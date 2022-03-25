using System;
using static System.Console;

namespace Булеан
{
    internal class Program
    {
        public static int[] a = new int[100];
        public static int[] Enter(int x, int[] b)
        {
            for (int i = 1; i <= x; i++)
            {
                Write("Enter element b[{0}] = ", i);
                b[i] = int.Parse(ReadLine());
            }
            return b;
        }
        public static void Out(int k, int[] b)
        {
            for (int i = 1; i <= k; i++)
            {
                Write(b[a[i]]);
            }
            WriteLine();
        }
        public static void Boolean(int i, int x, int k, int[] b)
        {
            for (int j = a[i - 1] + 1; j <= x; j++)
            {
                a[i] = j;
                if (i == k) Out(k, b);
                else Boolean(i + 1, x, k, b);
            }
            
        }
        static void Main(string[] args)
        {
            Write("Enter the size of asemble: ");
            int x = int.Parse(ReadLine());
            int[] b = new int[x+1];
            b = Enter(x, b);
            a[0] = 0;

            WriteLine("[]");

            for(int k=1; k<=x; k++)
            {
                Boolean(1, x, k, b);
            }
        }
    }
}
