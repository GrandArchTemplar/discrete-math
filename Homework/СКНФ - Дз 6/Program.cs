using System;
using static System.Console;
using static System.Math;

namespace Этап6_СКНФ
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string ans = "";
            string[] symbols = new string[] { "a", "b", "c", "d", "e" };
            WriteLine("Enter the value of k = ");
            int k = int.Parse(ReadLine());
            double m = Pow(2, k);
            int n = (int)m;
            int[,] table = new int[n, k + 1];
            for (int i = 0; i < n; i++)
            {
                string[] x_y = ReadLine().Split(new[] { ' ' });
                for (int j = 0; j <= k; j++)
                {
                    table[i, j] = int.Parse(x_y[j]);
                }
                x_y = null;
            }
            string ans1 = "";
            for (int i = 0; i < n; i++)
            {
                
                if (table[i, k] == 0)
                {
                    
                    for (int j = 0; j < k; j++)
                    {
                        
                        if (table[i, j] == 0)
                        {
                            ans1 += symbols[j];
                        }
                        else
                        {
                            ans1 += "-" + symbols[j];
                        }
                        ans1 += "+";
                    }
                    ans1 = ans1.Remove(ans1.Length - 1, 1);
                    ans1 = "("+ans1+")";

                }
                ans += ans1;
                ans1 = null;
            }
            WriteLine(ans);
        }
    }
}
