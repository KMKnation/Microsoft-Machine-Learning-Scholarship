import os
import re

SENTENCE_PATTERN =  re.compile(r'\d+', re.M)

transcript_file = '/home/hb/machinelearning/Azure/resource/Welcome+to+Introduction+to+Machine+Learning+on+Azure+Subtitles/3 - 0 00 11983 Udacity ML Course Lesson0 FINAL V3 - lang_en.srt'

transcript = ''
with open(transcript_file, 'r') as file:
    lines = file.readlines()
    # print(lines)
    for line in lines:
        a = SENTENCE_PATTERN.findall(line)
        if len(a) == 0:
            sentence = line.lstrip('\n')
            sentence = sentence.rstrip('\n')
            transcript += ' '+sentence


print(transcript)