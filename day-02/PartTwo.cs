// SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
//
// SPDX-License-Identifier: GPL-3.0-or-later

using System;
using System.Linq;

namespace day_02
{
    class PartTwo
    {
        static void Main(string[] args)
        {
            char[] delimiters = { '-', ' ', ':' };
            int cont = 0;
            string[] lines = System.IO.File.ReadAllLines(args[0]);
            foreach (string line in lines)
            {
                string[] data = line.Split(delimiters);
                int min = Int32.Parse(data[0]) - 1;
                int max = Int32.Parse(data[1]) - 1;
                char target = char.Parse(data[2]);
                string text = data[4];
                int freq = 0;
                if (text[min] == target)
                {
                    freq++;
                }
                if (text[max] == target)
                {
                    freq++;
                }
                if (freq == 1)
                {
                    cont++;
                }
            }
            Console.WriteLine(cont);
        }
    }
}
