using System;
using static System.Console;
using static System.Math;

namespace Этап5___СДНФ
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
            for (int i = 0; i < n; i++)
            {
                if (table[i, k] == 1)
                {
                    for (int j = 0; j < k; j++)
                    {
                        if (table[i, j] == 1)
                        {
                            ans += symbols[j];
                        }
                        else
                        {
                            ans += "(-" + symbols[j] + ")";
                        }
                    }
                    ans += "+";

                }

            }
            WriteLine(ans.Remove(ans.Length-1, 1));
        }
    }
}

