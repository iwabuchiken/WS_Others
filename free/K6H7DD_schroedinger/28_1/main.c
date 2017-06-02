/*
 * file : C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1\main.c
 * at : 2017/06/02 18:13:21
 * in project : res free# / K6H7DD 28#2 / シュレーディンガー方程式 / 20170602_180556
 *
 * <usage>
pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1
gcc main.c -o main.exe
main.exe

 *
 */


#include "include/utils.h"

void generate_Solutions() {

	double psy_0 = 0.0;
	double f_0 = 0.1;

	double V;	// potential energy

	double E = 2.6760079;	// Energy of the electron

	double tick = 0.1;
//	float tick = 0.1;

	int i;		// iterator

	int width = 20;

	int max = width / tick;	// x coordinate where psy gets to be zero
//	double max = 20;	// x coordinate where psy gets to be zero
//	int max = 20;	// x coordinate where psy gets to be zero

	double* psys;
	double* fs;

	psys = malloc(sizeof(double) * (max / tick));
	fs = malloc(sizeof(double) * (max / tick));

	psys[0] = psy_0;
	fs[0] = f_0;

	printf("[%s:%d] psys[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, psys[0]);
	printf("[%s:%d] fs[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, fs[0]);


	// loop
	//ref https://stackoverflow.com/questions/18175513/how-to-increment-a-for-loop-with-a-decimal-value-in-c
	for (i = 1; i <= max; i ++) {
//	for (i = 1; i < max; i ++) {
//	for (i = 0.1; i < max; i += tick) {
//	for (i = 0.1; i < max; i = i + tick) {

//		//debug
//		printf("[%s:%d] i = %d\n", basename(__FILE__, '\\'), __LINE__, i);
////		printf("[%s:%d] i = %f\n", basename(__FILE__, '\\'), __LINE__, i);


		// V : potential energy
		if (i * tick < 5 || i * tick >= 15) V = 50.0;
//		if (i < 5 || i >= 15) V = 50.0;
		else V = 0.0;



	}//for (i = 0; i < 20; ++i) {




	// free
	free(psys);

	//debug
	printf("[%s:%d] generate_Solutions() ---> done\n", basename(__FILE__, '\\'), __LINE__);


}//void generate_Solutions()


int main(int argc, char *argv[]) {

	/********************************************************
	 *
	 * operations
	 *
	*********************************************************/
	generate_Solutions();

	printf("[%s:%d] yes, done\n", basename(__FILE__, '\\'), __LINE__);
//	printf("[%s:%d] done\n", __FILE__, __LINE__);


	return 0;

}
