void setup() {
    pinMode(13, OUTPUT);
}

void loop() {
    digitalWrite(13, HIGH);
    delay (1000000);
    digitalWrite(13, LOW);
    delay (1000000);
    digitalWrite(13, HIGH);
    delay (25);
    digitalWrite(13, LOW);
    delay (25);
}
