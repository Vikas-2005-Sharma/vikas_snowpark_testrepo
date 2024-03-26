from snowflake.snowpark.session import Session 
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col
from config import snowflake_conn_prop_local as snowflake_conn_prop

def hello(session: Session) -> DataFrame:
    df = session.table("demodb.dev.customers")
    #df = df.groupBy("STATE").count()
    return df

# For local debugging
if __name__ == "__main__":
    session = Session.builder.configs(snowflake_conn_prop).create()
    print (hello (session).show())