using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Этап8___BFS
{
    internal class Program
    {
        public static void Input(string k, ref int a, ref int b, ref int c)
        {
            string[] x_y = k.Split(new[] { ' ' });
            a = int.Parse(x_y[0]);
            b = int.Parse(x_y[1]);
            c = int.Parse(x_y[2]);
        }
        public static int[] BFS(List<int>[] graph, int n, int k, int to, int[,] edge, bool[] visited)
        {
            int[] d = new int[n + 1];
            for (int i = 1; i <= n; i++)
            {
                d[i] = 10000;
            }
           
            Queue<int> vs = new Queue<int>();
            vs.Enqueue(k);
            d[k] = 0;
            d[to] = 0;
            int l = 0;
            while (vs.Count > 0)
            {
                l = vs.Dequeue();
                visited[l] = true;
                for (int i = 1; i <= n; i++)
                {
                    if (d[i]>edge[k,l]+d[k])
                    {
                        d[i]=edge[k,l] + d[k];
                    }
                }
                
                for (int i = 0; i < graph[l].Count; i++)
                {
                    if (!visited[graph[l][i]])
                    {
                        vs.Enqueue(graph[l][i]);
                    }
                }
            }
            return d;
        }
        static void Main(string[] args)
        {

            int n, m, k;
            string[] x_y = ReadLine().Split(new[] { ' ' });
            n = int.Parse(x_y[0]);
            m = int.Parse(x_y[1]);
            k = int.Parse(x_y[2]);
            x_y = null;

            var graph = new List<int>[n + 1];
            for (int i = 1; i <= n; i++)
            {
                graph[i] = new List<int>();
            }
            int[,] edge = new int[n + 1, n + 1];
            int a = 0, b = 0, c = 0;
            for (int i = 1; i <= m; i++)
            {
                string t = ReadLine();
                Input(t, ref a, ref b, ref c);
                graph[a].Add(b);
                edge[a, b] = c;
            }

            for (int i = 1; i <= n; i++)
            {
                bool[] visited = new bool[n + 1];
                for (int j = 1; j <= n; j++)
                {
                    visited[j] = false;
                }
                int[]d = BFS(graph, n, k, i, edge, visited);
                
                Write(d[i] + " ");

            }
        }
    }
}
