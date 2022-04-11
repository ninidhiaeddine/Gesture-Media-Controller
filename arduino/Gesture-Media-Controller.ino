String data;

#define TxD 1
#define RxD 0

void initializeBluetooth();

void setup()
{
  initializeBluetooth();
}

void loop()
{
  //readData();
  sendMediaRequest();
}

void initializeBluetooth()
{
  // define pin modes:
  pinMode(RxD, INPUT);
  pinMode(TxD, OUTPUT);

  // set baud rate:
  Serial.begin(9600);
}

void sendMediaRequest()
{
  Serial.println("PLAY_PAUSE");
  delay(2000);
  Serial.println("VOLUME_UP");
  delay(2000);
}
