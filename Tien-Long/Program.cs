using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using static System.Console;

namespace Huffman
{
    internal class Program
    {
        static void Main()
        {
            Console.WriteLine("Please enter the string:");
            string input = Console.ReadLine();
            HuffmanTree huffmanTree = new HuffmanTree();

            // Build the Huffman tree
            huffmanTree.Build(input);

            // Encode
            Dictionary<char, string> encoded = huffmanTree.Encode(input);

            
            foreach (KeyValuePair<char, string> bit in encoded)
            {
                WriteLine("{0} {1}", bit.Key, bit.Value);
                
            }
            Console.WriteLine();
        }
    }
    public class Node
    {
        public char Symbol { get; set; }
        public int Frequency { get; set; }
        public Node Right { get; set; }
        public Node Left { get; set; }
        public List<bool> Traverse(char symbol, List<bool> data)
        {
            // Leaf
            if (Right == null && Left == null)
            {
                if (symbol.Equals(this.Symbol))
                {
                    return data;
                }
                else
                {
                    return null;
                }
            }
            else
            {
                List<bool> left = null;
                List<bool> right = null;

                if (Left != null)
                {
                    List<bool> leftPath = new List<bool>();
                    leftPath.AddRange(data);
                    leftPath.Add(false);
                    left = Left.Traverse(symbol, leftPath);
                }

                if (Right != null)
                {
                    List<bool> rightPath = new List<bool>();
                    rightPath.AddRange(data);
                    rightPath.Add(true);
                    right = Right.Traverse(symbol, rightPath);
                }
                if (left != null)
                {
                    return left;
                }
                else
                {
                    return right;
                }
            }
        }
    }

    public class HuffmanTree
    {
        private List<Node> nodes = new List<Node>();
        public Node Root { get; set; }
        public Dictionary<char, int> Frequencies = new Dictionary<char, int>();
        public void Build(string source)
        {
            for (int i = 0; i < source.Length; i++)
            {
                if (!Frequencies.ContainsKey(source[i]))
                {
                    Frequencies.Add(source[i], 0);
                }

                Frequencies[source[i]]++;
            }

            foreach (KeyValuePair<char, int> symbol in Frequencies)
            {
                nodes.Add(new Node() { Symbol = symbol.Key, Frequency = symbol.Value });
            }

            while(nodes.Count > 1)
            {
                List<Node> orderedNodes = nodes.OrderBy(node => node.Frequency).ToList<Node>();
                if(orderedNodes.Count >= 2)
                {
                    // Take fisrt two items
                    List<Node> taken = orderedNodes.Take(2).ToList<Node>();

                    // Create a parent node by combining the frequencies
                    Node parent = new Node()
                    {
                        Symbol = '*',
                        Frequency = taken[0].Frequency + taken[1].Frequency,
                        Left = taken[0],
                        Right = taken[1]
                    };

                    nodes.Remove(taken[0]);
                    nodes.Remove(taken[1]);
                    nodes.Add(parent);
                }
                this.Root = nodes.FirstOrDefault();
            }
        }

        public Dictionary<char, string> Encode(string source)
        {
            
            Dictionary<char, string> bits = new Dictionary<char, string>();

            for (int i = 0; i < source.Length; i++)
            {
                if (!bits.ContainsKey(source[i]))
                {
                    List<bool> encodedSymbol = this.Root.Traverse(source[i], new List<bool>());
                    string t = string.Empty;
                    BitArray bit = new BitArray(encodedSymbol.ToArray());
                    foreach (bool b in bit)
                    {
                        int k = (b ? 1 : 0);
                        t += k.ToString();
                    }
                    bits.Add(source[i], t);
                }
                
            }
            return bits;
        }
    }
}
