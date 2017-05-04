/*
 *
pushd C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\10_1
gcc 10_1.c -o 10_1.exe
gcc 10_1.c -o 10_1.exe -DNMAX=100

* ref console parameter https://www.grapecity.com/tools/support/powernews/column/clang/014/page03.htm

 */

#include <stdio.h>

#ifndef UTILS_H_
//#define UTILS_H_
//#include "../../utils/utils.h"
#include "../../../utils/utils.h"
#endif

//#define NMAX
//#define NMAX 20

int main() {

#ifdef NMAX

	printf("[%s:%d] NMAX => %d\n", basename(__FILE__, '\\'), __LINE__, NMAX);

#else

	printf("[%s:%d] NMAX => NOT defined\n", basename(__FILE__, '\\'), __LINE__);

#endif
//	if (NMAX) {
//
//		printf("[%s:%d] NMAX => %d\n", basename(__FILE__, '\\'), __LINE__, NMAX);
//
//	} else {//if (NMAX)
//
//		printf("[%s:%d] NMAX => NOT defined\n", basename(__FILE__, '\\'), __LINE__);
//
//	}//if (NMAX)

//	printf("[%s:%d] NMAX => %d\n", basename(__FILE__, '\\'), __LINE__, NMAX);

	printf("[%s:%d] done\n", basename(__FILE__, '\\'), __LINE__);


	return 0;

}
