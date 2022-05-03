using System;
using static System.Console;


namespace Binaryrelation
{
    internal class Program
    {
        private static bool IsIn(int[][] b, int x, int y)
        {
            for (int i = 0; i < b.Length; i++)
            {
                if (b[i][0] == x && b[i][1] == y)
                {
                    return true;
                }
            }
            return false;
        }
        public static string transitivily(int[][] b, int y)
        {
            int[] s = new int[y];
            for (int i = 0; i < y; i++)
            {
                s[i] = b[i][1];
            }
            int[] c = new int[y];

            for (int i = 0; i < y; i++)
            {
                c[i] = b[i][0];
            }
            for (int i = 0; i < y; i++)
            {
                if (!IsIn(b, s[i], s[i]) || !IsIn(b, c[i], c[i]))
                {

                    return "not transitibily";
                }
            }
            return "transitivily";

        }
        public static string symmetry(int[][] b, int y)
        {
            int[] s = new int[y];
            for (int i = 0; i < y; i++)
            {
                s[i] = b[i][1];
            }
            int[] c = new int[y];
            for (int i = 0; i < y; i++)
            {
                c[i] = b[i][0];
            }
            for (int i = 0; i < y; i++)
            {
                if (!IsIn(b, s[i], c[i]))
                {
                    return "not symmetry";
                }
            }
            return "symmetry";
        }
        public static string reflexivity(int[][] b, int y)
        {
            int[] c = new int[y];
            for (int i = 0; i < y; i++)
            {
                c[i] = b[i][0];
            }
            for (int i = 0; i < y; i++)
            {
                if (!IsIn(b, c[i], c[i]))
                {
                    return "not reflexivity";
                }
            }
            return "reflexivity";
        }

        static void Main(string[] args)
        {
            string[] x_y = ReadLine().Split(new[] { ' ' }); // nhập dãy số vào mảng, nhập string được chia cắt 
            int x = int.Parse(x_y[0]);                      // вершин
            int y = int.Parse(x_y[1]);
            if (y <= Math.Pow(2, x))
            {
                int[][] b = new int[y][];             // b[][] = [[1,2], [3,4], ....] : ребер
                for (int i = 0; i < y; i++)
                {
                    x_y = null;
                    x_y = ReadLine().Split(new[] { ' ' });
                    b[i] = new int[] { int.Parse(x_y[0]), int.Parse(x_y[1]) };
                }
                //WriteLine(b[2][0]);
                WriteLine(transitivily(b, y));
                WriteLine(symmetry(b, y));
                WriteLine(reflexivity(b, y));
            }
            else
            {
                WriteLine("ERROR!!");
            }
        }
    }
}
