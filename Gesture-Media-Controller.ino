int LED = 13;
String data;

void initializeBluetooth();
void readData();
void playMusic();
void stopMusic();

void setup() 
{   
  initializeBluetooth();
}

void loop() 
{
  readData(); 
}

void initializeBluetooth()
{
  Serial.begin(9600);  
  Serial.println("Ready to connect\nDefualt password is 1234 or 0000"); 

  // initialize led light:
  pinMode(LED, OUTPUT);
}
