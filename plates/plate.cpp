 // Initialize the library using United States style license plates.
 // You can use other countries/regions as well (for example: "eu", "au", or "kr")
 
 #include<alpr.h>
 
 alpr::Alpr openalpr("us", "/usr/share/openalpr/config/openalpr.defaults.conf");

 
int main()
{return 0;}
