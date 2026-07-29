#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

/**
 * 生成服从泊松分布的随机数
 * 使用 Knuth 算法
 * 
 * @param lambda 泊松分布的参数 λ (lambda > 0)
 * @return 服从泊松分布的随机整数
 */
int poisson_random(double lambda) {
    double L = exp(-lambda);
    int k = 0;
    double p = 1.0;
    
    do {
        k++;
        p *= (double)rand() / RAND_MAX;
    } while (p > L);
    
    return k - 1;
}

int main() {
    // 初始化随机数种子
    srand((unsigned int)time(NULL));
    
    double lambda = 5.0;  // 泊松分布参数
    int count = 10;       // 生成随机数的个数
    
    printf("泊松分布随机数生成器 (λ = %.2f)\n", lambda);
    printf("生成 %d 个随机数:\n", count);
    printf("----------------------------\n");
    
    for (int i = 0; i < count; i++) {
        int random_num = poisson_random(lambda);
        printf("第 %2d 个: %d\n", i + 1, random_num);
    }
    
    printf("----------------------------\n");
    
    // 统计测试：生成大量样本并计算平均值
    int samples = 10000;
    long sum = 0;
    
    for (int i = 0; i < samples; i++) {
        sum += poisson_random(lambda);
    }
    
    double mean = (double)sum / samples;
    printf("\n统计测试 (%d 个样本):\n", samples);
    printf("理论均值 (λ): %.2f\n", lambda);
    printf("实际均值: %.2f\n", mean);
    
    return 0;
}
