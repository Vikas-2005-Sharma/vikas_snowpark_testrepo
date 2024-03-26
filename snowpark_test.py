from snowflake.snowpark.session import Session 
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col

def hello(session: Session) -> DataFrame:
    df = session.table("demodb.dev.customers")
    df = df.groupBy("STATE").count()
    return df

# For local debugging
if __name__ == "__main__":
    session = Session.builder.configs( {
   "account": "jyvwqoq-lr08285",
   "user": "Vikas2005S",
   "password": "Prophet1$",
   "database": "TEST_DB",
   "schema": "TEST_SCHEMA",
   "warehouse": "COMPUTE_WH",
   "role":"ACCOUNTADMIN",
}).create()
    print (hello (session).show())
