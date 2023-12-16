---
layout: post
disqus: y
title: Moon Orbits Earth String to Double
---

```c++
#include <iostream>   // std::cout
#include <string>     // std::string, std::stod

int main ()
{
  std::string orbits ("365.24 29.53");

  std::string::size_type sz;     // alias of size_t

  double earth = std::stod (orbits,&sz);

  double moon = std::stod (orbits.substr(sz));

  std::cout<<moon;

  std::cout << "The moon completes " << (earth/moon) << " orbits per Earth year.\n";
  return 0;
}
```


std::stod(orbits, &sz): This line converts the initial part of the string (orbits) to a double (earth). The sz variable is used to store the position of the first character not considered in the conversion.

std::stod(orbits.substr(sz)): This line converts the substring starting from the position indicated by sz to the end of the string. This substring represents the second number in the original string (moon).

The program then outputs the Moon's orbit and the ratio of the Earth's orbit to the Moon's orbit.

Keep in mind that the provided string must follow the expected format (two space-separated numbers) for this code to work correctly. If the input format is different, you may need to adjust the code accordingly.
