
import motor
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost/to_do_list?retryWrites=true&w=majority")
db = client.get_database("to_do_list")