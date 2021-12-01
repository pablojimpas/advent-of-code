// SPDX-FileCopyrightText: 2020 Pablo Jiménez Pascual <pablo@jimpas.me>
//
// SPDX-License-Identifier: GPL-3.0-or-later

using System;
using System.Linq;

namespace day_02
{
    class PartOne
    {
        static void Main(string[] args)
        {
            char[] delimiters = { '-', ' ', ':' };
            int cont = 0;
            string[] lines = System.IO.File.ReadAllLines(args[0]);
            foreach (string line in lines)
            {
                string[] data = line.Split(delimiters);
                int min = Int32.Parse(data[0]);
                int max = Int32.Parse(data[1]);
                char target = char.Parse(data[2]);
                string text = data[4];
                int freq = text.Count(f => (f == target));
                if (freq >= min && freq <= max)
                {
                    cont++;
                }
            }
            Console.WriteLine(cont);
        }
    }
}
