import paho.mqtt.client as mqtt

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('15780z5838/')
    else:
        print('Bad connection.Code:', rc)

def on_message(mqtt_client, userdata, msg):
    print(f'Recieved message on topic: {msg.topic} with payload: {msg.payload}')

client =  mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect =  on_connect
client.on_message = on_message
client.username_pw_set("15780z5838", "250bemorst")
client.connect(
    host="b37.mqtt.one",
    port=1883,
    keepalive=60,
)