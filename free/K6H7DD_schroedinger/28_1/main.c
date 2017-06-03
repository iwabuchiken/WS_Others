/*
 * file : C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1\main.c
 * at : 2017/06/02 18:13:21
 * in project : res free# / K6H7DD 28#2 / シュレーディンガー方程式 / 20170602_180556
 *
 * <usage>
pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1\data
pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1
gcc main.c -o main.exe
main.exe
main.exe 2.6760079

## gnuplot
cd "C:/WORKS_2/WS/WS_Others/free/K6H7DD_schroedinger/28_1/data"

plot "psys_fs.20170602_220219.dat" u 1, "psys_fs.20170602_220219.dat" u 2
fname = "psys_fs.20170602_220759.E-2.6660079.dat"
fname = "psys_fs.20170602_221926.E-2.7215891.dat"
plot fname u 1 with lines lw 1, fname u 2 with lines lw 1

load "C:/WORKS_2/WS/WS_Others/free/K6H7DD_schroedinger/28_1/shooting-method.plt"

### xyzzy
C:\WORKS_2\Programs\freeware\xyzzy\xyzzy C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1\shooting-method.plt

 *
 */


#include "include/utils.h"

void exec_Generate_Solutions
//(double E, double* psys, double* fs);
(double E, double tick, double* psys, double* fs, int max);

void generate_Solutions();

void generate_Solutions_2(double E);
//void generate_Solutions_2();

//int generate_Data(double* psys, double* fs);
int generate_Data(double* psys, double* fs, double E, double tick, int width);
//int generate_Data(psys, fs, E, tick, width)

/*
 * @return
 * -1	=> file can't be opened
 */
//int generate_Data(double* psys, double* fs) {
int generate_Data
(double* psys, double* fs, double E, double tick, int width) {

	/********************************************************
	 *
	 * setup : vars
	 *
	*********************************************************/
	char fpath[100];

	int max = width / tick;

	int i;	// iterator

//	sprintf(fpath, "data/psys_fs.%2.7f.%s.dat",
	sprintf(fpath, "data/psys_fs.%s.E-%2.7f.dat",
			get_Time_Label__Now(), E);
//			E,
//			get_Time_Label__Now());
//	sprintf(fpath, "psys_fs.%s.dat", get_Time_Label__Now());

	printf("[%s:%d] fpath => '%s'\n", basename(__FILE__, '\\'), __LINE__, fpath);


	/********************************************************
	 *
	 * file io
	 *
	*********************************************************/
	//ref http://www9.plala.or.jp/sgwr-t/c/sec17.html
	FILE* f_dst = fopen(fpath, "w");

	if (f_dst == NULL) {

		printf("[%s:%d] file can't be opened => '%s'\n",
				basename(__FILE__, '\\'), __LINE__, fpath);

//		printf("file can't be opened => '%s'\n", );
		exit(EXIT_FAILURE);	/* (3)エラーの場合は通常、異常終了する */

	}

//	fp = fopen("/tmp/test.txt", "w+");
//	fprintf(f_dst, "This is testing for fprintf...\n");

	/********************************************************
	 *
	 * write data
	 *
	*********************************************************/
	// header
	fprintf(f_dst,
			"# psys fs (E = %2.7f / tick = %1.2f / width = %d / max = %d)\n",
			E, tick, width, max);
//	fputs("# psys fs\n", f_dst);
//	fputs("This is testing for fputs...\n", fp);

	// body
	for (i = 0; i < max; ++i) {

		fprintf(f_dst,
				"%2.7f %2.7f\n",
				psys[i], fs[i]);


	}


	/********************************************************
	 *
	 * close file
	 *
	*********************************************************/
	fclose(f_dst);


}//int generate_Data(double* psys, double* fs)

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

void generate_Solutions_2(double E) {
//void generate_Solutions_2() {

//	double E = 2.6660079;	// Energy of the electron
//	double E = 2.6760079;	// Energy of the electron

	double tick = 0.1;

	int width = 20;

	int max = width / tick;	// x coordinate where psy gets to be zero

	double* psys;
	double* fs;

	// malloc
	psys = malloc(sizeof(double) * max);
	fs = malloc(sizeof(double) * max);

	// execute
//	exec_Generate_Solutions(E, psys, fs);
	exec_Generate_Solutions(E,tick, psys, fs, max);
//	exec_Generate_Solutions(E,tick, psys, fs);

	printf("[%s:%d] exec_Generate_Solutions => done\n", basename(__FILE__, '\\'), __LINE__);

	//debug
	printf("[%s:%d] psys[0] = %2.7f / fs[0] = %2.7f\n",
			basename(__FILE__, '\\'), __LINE__, psys[0], fs[0]);

//	//debug
//	int i;
//
//	for (i = 0; i < 10; ++i) {
//
//		printf("[%s:%d] psys[%d] = %2.7f / fs[%d] = %2.7f\n",
//					basename(__FILE__, '\\'), __LINE__,
//					i+100, psys[i+100], i+100,  fs[i+100]);
//
//	}
//	printf("[%s:%d] psys[100] = %2.7f / fs[100] = %2.7f\n",
//			basename(__FILE__, '\\'), __LINE__, psys[100], fs[100]);

	/********************************************************
	 *
	 * gen file
	 *
	*********************************************************/
	generate_Data(psys, fs, E, tick, width);

	//debug
	printf("[%s:%d] generate_Solutions_2() ---> done\n", basename(__FILE__, '\\'), __LINE__);


}//void generate_Solutions()

void exec_Generate_Solutions
//(double E, double* psys, double* fs) {
//(double E, double tick, double* psys, double* fs) {
(double E, double tick, double* psys, double* fs, int max) {

	double psy_0 = 0.0;
	double f_0 = 0.1;

	double V;	// potential energy

//	double E = 2.6760079;	// Energy of the electron

//	double tick = 0.1;
//	float tick = 0.1;

	int i;		// iterator

//	int width = 20;

//	int max = width / tick;	// x coordinate where psy gets to be zero
//	double max = 20;	// x coordinate where psy gets to be zero
//	int max = 20;	// x coordinate where psy gets to be zero

//	printf("[%s:%d] max = %d\n", basename(__FILE__, '\\'), __LINE__, max);


//	double* psys;
//	double* fs;

//	psys = malloc(sizeof(double) * max);
//	fs = malloc(sizeof(double) * max);
//	psys = malloc(sizeof(double) * (max / tick));
//	fs = malloc(sizeof(double) * (max / tick));

	double psy_prev = psy_0;
	double f_prev = f_0;

	double psy_cur;
	double f_cur;

	double h2_2m = 38.14;

	psys[0] = psy_0;
	fs[0] = f_0;

//	printf("[%s:%d] psys[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, psys[0]);
//	printf("[%s:%d] fs[0] => %2.7f\n", basename(__FILE__, '\\'), __LINE__, fs[0]);


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

//		printf("[%s:%d] psy_cur = %2.7f / f_cur = %2.7f\n",
//				basename(__FILE__, '\\'), __LINE__, psy_cur, f_cur);


		// update prev
		psy_prev	= psy_cur;
		f_prev		= f_cur;

	}//for (i = 0; i < 20; ++i) {


	//debug
	printf("[%s:%d] psys[%d] = %2.7f / fs[%d] = %2.7f\n",
			basename(__FILE__, '\\'), __LINE__,
			(max - 1), psys[max - 1], (max - 1), fs[max - 1]);
//	printf("[%s:%d] psys[100] = %2.7f / fs[100] = %2.7f\n",
//			basename(__FILE__, '\\'), __LINE__, psys[100], fs[100]);
//			basename(__FILE__, '\\'), __LINE__, psys, fs);


//	// free
//	free(psys);
//	free(fs);

	//debug
	printf("[%s:%d] exec_Generate_Solutions() ---> done\n", basename(__FILE__, '\\'), __LINE__);


}//exec_Generate_Solutions

void exec_Test_Malloc(double* test) {

//	test = malloc(sizeof(double) * 10);

	test[0] = 2.345;

	printf("[%s:%d] test[0] = %f\n", basename(__FILE__, '\\'), __LINE__, test[0]);


}

void test_Malloc() {

	double* test;

	test = malloc(sizeof(double) * 10);

	exec_Test_Malloc(test);

	printf("[%s:%d] test[0] = %f\n", basename(__FILE__, '\\'), __LINE__, test[0]);


}


int main(int argc, char *argv[]) {

//	printf("[%s:%d] argv[0] = '%s'\n", basename(__FILE__, '\\'), __LINE__, argv[0]);

	/********************************************************
	 *
	 * validate : args
	 *
	*********************************************************/
	if (argc < 2) {

		printf("[%s:%d] <usage> main.exe [double E]\n", basename(__FILE__, '\\'), __LINE__);

		return -1;

	}//if (argc < 2)

	/********************************************************
	 *
	 * operations
	 *
	*********************************************************/
	//ref https://www.google.co.jp/search?q=c+language+atof&oq=c+language+atof&aqs=chrome..69i64j5l2j0l3.4694j0j4&sourceid=chrome&ie=UTF-8#q=c+language+string+to+double
	generate_Solutions_2(atof(argv[1]));
//	generate_Solutions_2();
//	generate_Solutions();

//	test_Malloc();

	printf("[%s:%d] yes, done\n", basename(__FILE__, '\\'), __LINE__);
//	printf("[%s:%d] done\n", __FILE__, __LINE__);


	return 0;

}
