#include <iostream>
#include <fitsio.h>


using std::cout;
using std::endl;

int main(int argc, char** argv)
{
  float vers;
  float stat  = fits_get_version(&vers);
  cout << "fitsio version is:" << vers <<  endl;
}
