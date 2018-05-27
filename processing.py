import io
import os
import argparse
import numpy as np

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from pydub import AudioSegment
from pydub.silence import split_on_silence




def speech_to_text(speech_file):
    """Transcribe the given audio file."""
    # client = speech.SpeechClient()
    #
    # config = types.RecognitionConfig(
    #     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    #     language_code='en-US',
    #     sample_rate_hertz=18000,
    #     speech_contexts=[speech.types.SpeechContext(
    #         phrases=["sheshells", "sheshore"],
    #     )]
    # )
    #
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'audio_files',
    #     speech_file)
    #
    # with io.open(file_name, 'rb') as stream:
    #     requests = [speech.types.StreamingRecognizeRequest(
    #         audio_content=stream.read(),
    #     )]
    #
    # streaming_config = types.StreamingRecognitionConfig(config=config,
    #                                                     interim_results=True)
    #
    # responses = client.streaming_recognize(streaming_config, requests)
    #
    # i=0
    # j=0
    # k=0
    #
    # for response in responses:
    #     print('#' * 20)
    #     i=i+1
    #     print("i : " + str(i))
    #     for result in response.results:
    #         j = j + 1
    #         print("j : " + str(j))
    #         print('*' * 20)
    #         print('Finished: {}'.format(result.is_final))
    #         print('Stability: {}'.format(result.stability))
    #         for alternative in result.alternatives:
    #             k = k + 1
    #             print("k : " + str(k))
    #             print('='*20)
    #             print('Transcript: ' + alternative.transcript)
    #             print('Confidence: '+ str(alternative.confidence))
    #             print('is_final: ' + str(result.is_final))
    #
    #
    #             for word_info in alternative.words:
    #                 word = word_info.word
    #                 start_time = word_info.start_time
    #                 end_time = word_info.end_time
    #                 print('Word: {}, start_time: {}, end_time: {}'.format(
    #                     word,
    #                     start_time.seconds + start_time.nanos * 1e-9,
    #                     end_time.seconds + end_time.nanos * 1e-9))


    # Instantiates a client
    client = speech.SpeechClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        'audio_files',
        speech_file)

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()

    stream = [content]

    requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                for chunk in stream)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=18000,
        language_code='en-US'
        )
     #   speech_contexts=phrase_hints)
    streaming_config = types.StreamingRecognitionConfig(config=config,
                                           interim_results=True)

    responses = client.streaming_recognize(streaming_config, requests)

    result_array=[]
    result_string=None

    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.
        for result in response.results:
            print('Finished: {}'.format(result.is_final))
            print('Stability: {}'.format(result.stability))
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                print('Confidence: {}'.format(alternative.confidence))
                print(u'Transcript: {}'.format(alternative.transcript))
                result_array.append(alternative.transcript.split())
                result_string=alternative.transcript

                for word_info in alternative.words:
                    word = word_info.word
                    start_time = word_info.start_time
                    end_time = word_info.end_time
                    print('Word: {}, start_time: {}, end_time: {}'.format(
                        word,
                        start_time.seconds + start_time.nanos * 1e-9,
                        end_time.seconds + end_time.nanos * 1e-9))

    return [result_string, result_array]



def find_error(target, transcription, improve_sound):
    if target != transcription:
        return False



# print(find_error('she sells seashells by the seashore', speech_to_text('correct.wav')))


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(
#         description=__doc__,
#         formatter_class=argparse.RawDescriptionHelpFormatter)
#     parser.add_argument('stream', help='File to stream to the API')
#     args = parser.parse_args()
#     print(args)
#     speech_to_text(args.stream)
res = speech_to_text('wrong.wav')
print(res[0])
print(" ")
print(res[1])

flat_list = [item for sublist in res[1] for item in sublist]

print(" ")
array_flat_list = np.array(flat_list)






# speech_contexts=[speech.types.SpeechContext(
#     phrases=["sheshells by the sheshore"],
# )]




# # Each result is for a consecutive portion of the audio. Iterate through
# # them to get the transcripts for the entire audio file.
# for result in response.results:
#     # The first alternative is the most likely one for this portion.
#     print(u'Transcript: {}'.format(result.alternatives[0].transcript))
#     # print(u'Transcript: {}'.format(result.alternatives[1].transcript))
#     # print(u'Transcript: {}'.format(result.alternatives[2].transcript))
# return result.alternatives[0].transcript









# speech_contexts=[speech.types.SpeechContext(
#     phrases=["sheshells", "sheshore"],
# )]



# sound_file=AudioSegment.from_wav(file_name)
# # samples = np.array(sound_file.get_array_of_samples())
# #
# # print(len(samples))
# #
# # new_sound = sound_file._spawn(samples)
#
#
# audio_chunks = split_on_silence(sound_file,
#             # must be silent for at least half a second
#             min_silence_len=100,
#
#             # consider it silent if quieter than -16 dBFS
#             silence_thresh=-16
# )
#
# print(len(audio_chunks))
#
# for i, chunk in enumerate(audio_chunks):
#     out_file = "{}.wav".format(i)
#     print("exporting", out_file)
#     chunk.export(out_file, format="wav")