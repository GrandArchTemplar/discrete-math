using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Этап7___DFS
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
        public static int DFS(List<int>[] graph,int n, int k,int to, int[,] edge, int dicmin, int dic, bool[] visited)
        {
            Stack<int> vs = new Stack<int>();
            Stack<int> edges = new Stack<int>();
            vs.Push(k);
            int l = 0;
            int x = 0;
            while (vs.Count > 0)
            {
                l = vs.Pop();
                
                visited[l] = true;
                if (edges.Count>0)
                {
                    dic += edges.Pop();

                }
                
                if (l == to)
                {
                    if (dicmin > dic)
                    {
                        dicmin = dic;
                    }
                    dic = 0;
                }
                x = vs.Count;
                for (int i = 0; i < graph[l].Count; i++)
                {
                    if (!visited[graph[l][i]])
                    {
                        vs.Push(graph[l][i]);
                        edges.Push(edge[l, graph[l][i]]);
                    }

                }
                if(x==vs.Count)
                {
                    dic = 0;
                }
                

            }
            return dicmin;
        }
        static void Main(string[] args)
        {
            
            int n, m, k;
            string[] x_y = ReadLine().Split(new[] { ' ' });
            n = int.Parse(x_y[0]);
            m = int.Parse(x_y[1]);
            k = int.Parse(x_y[2]);
            x_y = null;

            var graph = new List<int>[n+1];
            for(int i=1; i<=n; i++)
            {
                graph[i] = new List<int>();
            }
            int[,] edge = new int[n+1,n+1];
            int a = 0, b = 0, c = 0;
            for (int i=1; i<=m; i++)
            {
                string t = ReadLine();
                Input(t, ref a, ref b, ref c);
                graph[a].Add(b);
                edge[a, b] = c;
            }

            int dicmin = 1000;
            int dic = 0;
            
            for (int i = 1; i <= n; i++)
            {
                bool[] visited = new bool[n + 1];
                for (int j = 1; j <= n; j++)
                {
                    visited[j] = false;
                }
                int o = DFS(graph, n, k, i, edge, dicmin, dic, visited);
                if (o == 1000)
                {
                    o = 0; 
                }
                Write(o + " ");

            }
        }
    }
}
