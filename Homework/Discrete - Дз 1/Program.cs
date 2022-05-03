using System;
using System.Collections;
using System.Collections.Generic;
using static System.Console;

namespace Discrete
{
    internal class Program
    {
        public static int[] Enter(int[] o, int x)
        {
            WriteLine("Enter value of sets:");
            for (int c = 0; c < x; c++)
            {
                Write("Enter value for element[{0}] : ", c);
                o[c] = int.Parse(ReadLine());
            }
            return o;
        }
        public static void homework01(int[] o, int[] a, char t)
        {
            int k = 0;
            List<int> mylist = new List<int>();
            if (t == 'u')
            {
                for (int d = 0; d < a.Length; d++)
                {
                    mylist.Add(a[d]);
                    k += 1;
                }
                for (int c = 0; c < o.Length; c++)
                {

                    int x = 0;
                    for (int d = 0; d < a.Length; d++)
                    {
                        if (a[d] != o[c])
                        {
                            x += 1;
                        }
                        if (x == a.Length)
                        {
                            mylist.Add(o[c]);
                            k += 1;
                        }
                    }
                    x = 0;
                }

            }
            if (t == 'i')
            {
                for (int c = 0; c < o.Length; c++)
                {

                    int x = 0;
                    for (int d = 0; d < a.Length; d++)
                    {
                        if (a[d] == o[c])
                        {
                            x += 1;
                        }
                        if (x > 0)
                        {
                            mylist.Add(o[c]);
                            k += 1;
                        }
                    }
                    x = 0;
                }
            }
            if (t == 's')
            {
                for (int c = 0; c < o.Length; c++)
                {

                    int x = 0;
                    for (int d = 0; d < a.Length; d++)
                    {
                        if (a[d] != o[c])
                        {
                            x += 1;
                        }
                        if (x == a.Length)
                        {
                            mylist.Add(o[c]);
                            k += 1;
                        }
                    }
                    x = 0;
                }
            }
            if (t == 'a')
            {
                for (int d = 0; d < a.Length; d++)
                {

                    int x = 0;
                    for (int c = 0; c < o.Length; c++)
                    {
                        if (a[d] != o[c])
                        {
                            x += 1;
                        }
                        if (x == o.Length)
                        {
                            mylist.Add(a[d]);
                            k += 1;
                        }
                    }
                    x = 0;
                }
            }
            for (int i = k - 1; i >= 0; i--)
            {
                for (int j = 1; j <= i; j++)
                    if (mylist[j - 1] > mylist[j])
                    {
                        int temp = mylist[j];
                        mylist[j] = mylist[j - 1];
                        mylist[j - 1] = temp;
                    }
            }
            foreach (int i in mylist)
            {
                Write(i + " ");
            }
        }
        static void Main(string[] args)
        {
            int a = int.Parse(ReadLine());
            int b = int.Parse(ReadLine());
            int[] x = new int[a];
            int[] y = new int[b];
            Enter(x, a);
            Enter(y, b);
            char t = char.Parse(ReadLine());
            homework01(x, y, t);

        }
    }
}
