#!/usr/bin/env ruby

sender = ARGV[0].scan(/(?<=from:)\+?\w+/).join
receiver = ARGV[0].scan(/(?<=to:)\+?\w+/).join
flags = ARGV[0].scan(/(?<=flags:)\-?\d+\:\-?\d+:\-?\d+:\-?\d+:\-?\d+/).join

text = sender + "," + receiver + "," + flags
puts text
