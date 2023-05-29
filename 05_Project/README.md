# Audio to Tree Alignment

In this project, I have ELAN files with time aligned transcription, and I have a test conllu file with 1227 sentences in it. Since both the files follow very different conventions it is very difficult to align them. Therefore, to do it automatically I followed few steps based on sent_id, text, text[spa], and text[orig] comments in conllu file and file_name, audio_file, text, text(spanish translation), annotation_number, and start_time-end_time of the sentences of ELAN files to match them with sentences in CoNLL file and assign timestamps to them. 
