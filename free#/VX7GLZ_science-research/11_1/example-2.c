/*
 *
pushd C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\11_1\
gcc example-2.c -o example-2.exe
example-2.exe > data.txt
example-2.exe

	file: C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\10_1\example-2.c
	from: C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\9_1\example-2.c

 *
 */
#include <stdio.h>
#include <math.h>

#ifndef UTILS_H_
#include "../../../utils/utils.h"
#endif


#define C0r     -0.743  // 計算する場所の中心座標（実数部）
#define C0i      0.1145 // 計算する場所の中心座標（虚数部）
#define VS       0.003  // 計算する場所の中心座標からの範囲（±VS）

#define NMAX     20000  // 計算の繰り返し上限
//#define NMAX     10000  // 計算の繰り返し上限
//#define NMAX     5000  // 計算の繰り返し上限
//#define NMAX     500  // 計算の繰り返し上限
//#define NMAX     50  // 計算の繰り返し上限
#define STEP     800.0  // 計算する刻み

int n_max;

double mandelbrot(double a, double b){

  double x = 0.0;
  double y = 0.0;
  double x1, y1;

  int n;

  for (n = 1; n <= n_max; n++) {
//  for (n = 1; n <= NMAX; n++) {
    x1 = x * x - y * y + a;
    y1 = 2.0 * x * y + b;
    if ( x1 * x1 + y1 * y1 > 4.0) return log(n); // 発散
    x = x1;
    y = y1;
  }
  return 0; // 計算の繰り返し上限到達

}

void show_usage() {

	printf("<Usage>\n", __FILE__, __LINE__);
	printf("\texample-2.exe [num of NMAX]\n", __FILE__, __LINE__);
	printf("\te.g.) xample-2.exe 1000\n", __FILE__, __LINE__);


}//show_usage()

/*
 * @return
 * -1	argument not given
 * -2	argument is not a numeric
 */
int _setup_nmax(int argc, char *argv[]) {

	if (argc < 2) {

		printf("[%s:%d] argument needed\n", basename(__FILE__, '\\'), __LINE__);

		show_usage();

		return -1;

	} else if (!is_numeric(argv[1])){//if (argc < 2)

		printf("[%s:%d] argument is not numeric: %s\n", basename(__FILE__, '\\'), __LINE__, argv[1]);

		show_usage();

		return -2;

	}//if (argc < 2)

	int given = atoi(argv[1]);

	n_max = given;

	return 1;

}//int _setup_nmax(int argc, char *argv[])

//ref argc,argv https://www.tutorialspoint.com/cprogramming/c_command_line_arguments.htm
int main(int argc, char *argv[]) {

	int result = _setup_nmax(argc, argv);

	if (result < 0) {

		printf("[%s:%d] setup => undone: %d\n", basename(__FILE__, '\\'), __LINE__, result);

		return -1;

	}

	/**********************

		calc

	**********************/
	double a, b;

	for (a = C0r-VS; a < C0r+VS; a += 2.0*VS/STEP) {
		for (b = C0i-VS; b < C0i+VS; b += 2.0*VS/STEP) {
		  printf("%1.14e %1.14e %1.14e\n", a, b, mandelbrot(a, b));
		}
		printf("\n"); // これがないとgnuplotでエラーが出る
	}

  return 0;

}
