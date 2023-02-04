import os
from azure.iot.hub import IoTHubModuleClient

def iothub_client_init():
    connection_string = os.getenv("IOTHUB_MODULE_CONNECTION_STRING")
    return IoTHubModuleClient.from_connection_string(connection_string)

def main():
    client = iothub_client_init()

    # Connect the client.
    client.connect()

    while True:
        # Wait for a message to arrive on input1.
        msg = client.receive_message()

        # Do something with the message.
        print("Message received: {}".format(msg.data))

        # Acknowledge the message.
        client.complete_message(msg)

if __name__ == "__main__":
    main()
