/*
 *
pushd C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\10_1\
gcc test_open-gnuplot.c -o test_open-gnuplot.exe
test_open-gnuplot.exe


C:\WORKS_2\Programs\gnuplot_4.6.7\bin\wgnuplot.exe

 *
 */

#include <stdio.h>


int main(int argc, char *argv[]) {

	char* exec_path = "C:/WORKS_2/Programs/gnuplot_4.6.7"
			"/bin/pgnuplot.exe";

	char* plot_command = "load \"C:/WORKS_2/WS/WS_Others/"
//			"free#/VX7GLZ_science-research/10_1/test.plt\" \"abc\"\n";
			"free#/VX7GLZ_science-research/10_1/test.plt\"\n";

	char storage[20];	//=> used for gets()


	FILE *fp = _popen(exec_path, "w");
//	FILE *fp = _popen("C:/gnuplot/bin/pgnuplot.exe", "w");

	if (fp == NULL) {

		printf("[%s:%d] fp ---> NULL\n", __FILE__, __LINE__);

		return -1;
	}

	printf("[%s:%d] plotting... Hit return key for quit\n",
			__FILE__, __LINE__);

	//test
	//ref http://www.natural-science.or.jp/article/20110818012440.php "グラフ描画"
//	fputs("abc = 14567", fp);
	fputs("abc = 14567\n", fp);	//=> works


	fputs(plot_command, fp);
//	fputs("load \"C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/10_1/test.plt\"\n", fp);
//	fputs("plot sin(x)\n", fp);

	fflush(fp);

//	cin.get(); //<------------------------------------- 一時停止のために入れる

	gets(storage);

	_pclose(fp);

	return 0;

}
