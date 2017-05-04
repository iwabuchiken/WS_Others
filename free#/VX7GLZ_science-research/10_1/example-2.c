/*
 *
pushd C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\10_1\
gcc example-2.c -o example-2.exe
example-2.exe > data.txt
example-2.exe
(took ---> 1.32 2017/05/03 17:08:59)


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

	printf("[%s:%d] NMAX => %d\n", basename(__FILE__, '\\'), __LINE__, NMAX);
	printf("[%s:%d] n_max => %d\n", basename(__FILE__, '\\'), __LINE__, n_max);

	return 0.0;

//  double x = 0.0;
//  double y = 0.0;
//  double x1, y1;
//
//  int n;
//
//  for (n = 1; n <= NMAX; n++) {
//    x1 = x * x - y * y + a;
//    y1 = 2.0 * x * y + b;
//    if ( x1 * x1 + y1 * y1 > 4.0) return log(n); // 発散
//    x = x1;
//    y = y1;
//  }
//  return 0; // 計算の繰り返し上限到達
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

	printf("[%s:%d] argc => %d\n", basename(__FILE__, '\\'), __LINE__, argc);

	printf("[%s:%d] argv[0] => '%s'\n", basename(__FILE__, '\\'), __LINE__, argv[0]);

	if (argc < 2) {

		printf("[%s:%d] argument needed\n", basename(__FILE__, '\\'), __LINE__);

		show_usage();

		return -1;

	} else if (!is_numeric(argv[1])){//if (argc < 2)

		printf("[%s:%d] argument needed\n", basename(__FILE__, '\\'), __LINE__);

		show_usage();

		return -2;

	}//if (argc < 2)

	int given = atoi(argv[1]);

	n_max = given;

	printf("[%s:%d] n_max set ---> %d\n", basename(__FILE__, '\\'), __LINE__, n_max);


	return 1;

}

//ref argc,argv https://www.tutorialspoint.com/cprogramming/c_command_line_arguments.htm
//int main() {
int main(int argc, char *argv[]) {

	//test
//	printf("[%s:%d] argc => %d\n", basename(__FILE__, '\\'), __LINE__, argc);
	int result = _setup_nmax(argc, argv);

	if (result < 0) {

		printf("[%s:%d] setup => undone: %d\n", basename(__FILE__, '\\'), __LINE__, result);

		return -1;

	}


	mandelbrot(0.1, 0.2);

	return 0;

	//] test end

//  double a, b;
//
//  for (a = C0r-VS; a < C0r+VS; a += 2.0*VS/STEP) {
//    for (b = C0i-VS; b < C0i+VS; b += 2.0*VS/STEP) {
//      printf("%1.14e %1.14e %1.14e\n", a, b, mandelbrot(a, b));
//    }
//    printf("\n"); // これがないとgnuplotでエラーが出る
//  }
//
//  return 0;

}
