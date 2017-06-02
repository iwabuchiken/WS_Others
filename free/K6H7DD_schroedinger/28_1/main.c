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

	double psy_prev = psy_0;
	double f_prev = f_0;

	double psy_cur;
	double f_cur;

	double h2_2m = 38.14;

	psys[0] = psy_0;
	fs[0] = f_0;

	printf("[%s:%d] psys[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, psys[0]);
	printf("[%s:%d] fs[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, fs[0]);


	// loop
	//ref https://stackoverflow.com/questions/18175513/how-to-increment-a-for-loop-with-a-decimal-value-in-c
	for (i = 1; i <= max; i ++) {

		// V : potential energy
		if (i * tick < 5 || i * tick >= 15) V = 50.0;
		else V = 0.0;

		// calc
		psy_cur = tick * f_prev + psy_prev;

		f_cur = -1 * tick * psy_prev * (E - V) / h2_2m + f_prev;

		psys[i]	= psy_cur;
		fs[i]	= f_cur;

		printf("[%s:%d] psy_cur = %2.7f / f_cur = %2.7f\n",
				basename(__FILE__, '\\'), __LINE__, psy_cur, f_cur);


		// update prev
		psy_prev	= psy_cur;
		f_prev		= f_cur;

	}//for (i = 0; i < 20; ++i) {




	// free
	free(psys);
	free(fs);

	//debug
	printf("[%s:%d] generate_Solutions() ---> done\n", basename(__FILE__, '\\'), __LINE__);


}//void generate_Solutions()

void generate_Solutions_2() {

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

	double psy_prev = psy_0;
	double f_prev = f_0;

	double psy_cur;
	double f_cur;

	double h2_2m = 38.14;

	psys[0] = psy_0;
	fs[0] = f_0;

	printf("[%s:%d] psys[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, psys[0]);
	printf("[%s:%d] fs[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, fs[0]);


	// loop
	//ref https://stackoverflow.com/questions/18175513/how-to-increment-a-for-loop-with-a-decimal-value-in-c
	for (i = 1; i <= max; i ++) {

		// V : potential energy
		if (i * tick < 5 || i * tick >= 15) V = 50.0;
		else V = 0.0;

		// calc
		psy_cur = tick * f_prev + psy_prev;

		f_cur = -1 * tick * psy_prev * (E - V) / h2_2m + f_prev;

		psys[i]	= psy_cur;
		fs[i]	= f_cur;

		printf("[%s:%d] psy_cur = %2.7f / f_cur = %2.7f\n",
				basename(__FILE__, '\\'), __LINE__, psy_cur, f_cur);


		// update prev
		psy_prev	= psy_cur;
		f_prev		= f_cur;

	}//for (i = 0; i < 20; ++i) {




	// free
	free(psys);
	free(fs);

	//debug
	printf("[%s:%d] generate_Solutions() ---> done\n", basename(__FILE__, '\\'), __LINE__);


}//void generate_Solutions()

void exec_Generate_Solutions
(double E, double tick, double* psys, double* fs) {

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

//	double* psys;
//	double* fs;

	psys = malloc(sizeof(double) * (max / tick));
	fs = malloc(sizeof(double) * (max / tick));

	double psy_prev = psy_0;
	double f_prev = f_0;

	double psy_cur;
	double f_cur;

	double h2_2m = 38.14;

	psys[0] = psy_0;
	fs[0] = f_0;

	printf("[%s:%d] psys[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, psys[0]);
	printf("[%s:%d] fs[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, fs[0]);


	// loop
	//ref https://stackoverflow.com/questions/18175513/how-to-increment-a-for-loop-with-a-decimal-value-in-c
	for (i = 1; i <= max; i ++) {

		// V : potential energy
		if (i * tick < 5 || i * tick >= 15) V = 50.0;
		else V = 0.0;

		// calc
		psy_cur = tick * f_prev + psy_prev;

		f_cur = -1 * tick * psy_prev * (E - V) / h2_2m + f_prev;

		psys[i]	= psy_cur;
		fs[i]	= f_cur;

		printf("[%s:%d] psy_cur = %2.7f / f_cur = %2.7f\n",
				basename(__FILE__, '\\'), __LINE__, psy_cur, f_cur);


		// update prev
		psy_prev	= psy_cur;
		f_prev		= f_cur;

	}//for (i = 0; i < 20; ++i) {




//	// free
//	free(psys);
//	free(fs);

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
