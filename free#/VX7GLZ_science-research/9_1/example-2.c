/*
 *
pushd C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\9_1\
gcc example-2.c -o example-2.exe
example-2.exe > data.txt
(took ---> 1.32 2017/05/03 17:08:59)


 *
 */
#include <stdio.h>
#include <math.h>

#define C0r     -0.743  // 計算する場所の中心座標（実数部）
#define C0i      0.1145 // 計算する場所の中心座標（虚数部）
#define VS       0.003  // 計算する場所の中心座標からの範囲（±VS）

//#define NMAX     20000  // 計算の繰り返し上限
//#define NMAX     10000  // 計算の繰り返し上限
#define NMAX     5000  // 計算の繰り返し上限
#define STEP     800.0  // 計算する刻み


double mandelbrot(double a, double b){
  double x = 0.0;
  double y = 0.0;
  double x1, y1;

  int n;

  for (n = 1; n <= NMAX; n++) {
    x1 = x * x - y * y + a;
    y1 = 2.0 * x * y + b;
    if ( x1 * x1 + y1 * y1 > 4.0) return log(n); // 発散
    x = x1;
    y = y1;
  }
  return 0; // 計算の繰り返し上限到達
}


int main() {
  double a, b;

  for (a = C0r-VS; a < C0r+VS; a += 2.0*VS/STEP) {
    for (b = C0i-VS; b < C0i+VS; b += 2.0*VS/STEP) {
      printf("%1.14e %1.14e %1.14e\n", a, b, mandelbrot(a, b));
    }
    printf("\n"); // これがないとgnuplotでエラーが出る
  }
  return 0;
}
