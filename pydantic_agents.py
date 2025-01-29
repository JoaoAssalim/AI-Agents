import os
import sqlite3
from load_dotenv import load_dotenv

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.groq import GroqModel

load_dotenv()


class DatabaseConn:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def run_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        explanation = f"Executed query: {query}"

        return result, explanation


class SQLResponse(BaseModel):
    sql_response: list
    explanation: str
    sql_query: str

model = GroqModel('llama-3.3-70b-versatile')

agent = Agent(
    model=model,
    result_type=SQLResponse,
    system_prompt=(
        "You are a specialist SQL query generator. "
        "You need to convert a user question into a valid SQL query. "
    ),
)

@agent.tool(retries=1)
def run_sql_query_in_database(ctx: RunContext, query: str) -> SQLResponse:
    """Run SQL query in database."""
    conn = DatabaseConn()
    result, explanation = conn.run_query(query)
    return SQLResponse(sql_response=result, explanation=explanation, sql_query=query)

result = agent.run_sync("Get all users names from table users;")
print(f"SQL DATA: {result.data.sql_response}")
print(f"EXPLANATION: {result.data.explanation}")
print(f"SQL QUERY: {result.data.sql_query}")