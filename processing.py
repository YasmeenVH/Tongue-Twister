import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types



def speech_to_text(speech_file):
    client = speech.SpeechClient()

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
        sample_rate_hertz=18000,
        speech_contexts=[speech.types.SpeechContext(
            phrases=["sheshells", "sheshore"],
        )]
    )

    file_name = os.path.join(
        os.path.dirname(__file__),
        'audio_files',
        speech_file)

    with io.open(file_name, 'rb') as stream:
        requests = [speech.types.StreamingRecognizeRequest(
            audio_content=stream.read(),
        )]
    streaming_config = types.StreamingRecognitionConfig(config=config,
                                                        interim_results=True)

    responses = client.streaming_recognize(streaming_config, requests)

    list_res = []
    string_res = ""
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
                list_res.append(alternative.transcript.split())
                string_res = alternative.transcript
    return [string_res, list_res]


def find_error(target, transcription, improve_sound):
    flat_list_transcribed = [item for sublist in transcription[1] for item in sublist]
    flat_list_actual = [item for sublist in target[1] for item in sublist]
    count_transcribed_1 = 0
    count_actual_1 = 0
    count_transcribed_2 = 0
    count_actual_2 = 0
    for word in flat_list_transcribed:
        if improve_sound[0] in word:
            count_transcribed_1 += 1
        if improve_sound[1] in word:
            count_transcribed_2 += 1
    for word in flat_list_actual:
        if improve_sound[0] in word:
            count_actual_1 += 1
        if improve_sound[1] in word:
            count_actual_2 += 1
    print([count_transcribed_1, count_transcribed_2, count_actual_1, count_actual_2])
    return "Detected " + str(float(count_transcribed_1)/count_actual_1*100) + "% of desired " + improve_sound[0] + " and " + str(float(count_transcribed_2)/count_actual_2*100) + "% of desired " + improve_sound[1]




    # # Instantiates a client
    # client = speech.SpeechClient()
    #
    # # The name of the audio file to transcribe
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'audio_files',
    #     name)
    #
    # # Loads the audio into memory
    # with io.open(file_name, 'rb') as audio_file:
    #     content = audio_file.read()
    #     audio = types.RecognitionAudio(content=content)
    #
    # # In practice, stream should be a generator yielding chunks of audio data.
    # stream = [content]
    # requests = (types.StreamingRecognizeRequest(audio_content=chunk)
    #             for chunk in stream)
    #
    # config = types.RecognitionConfig(
    #     encoding='LINEAR16',
    #     sample_rate_hertz=16000,
    #     language_code='en-US'
    #     # speech_contexts=[speech.types.SpeechContext(
    #     #     phrases=["sheshells by the sheshore"],
    #     # )]
    #     )
    #  #   speech_contexts=phrase_hints)
    # streaming_config = types.StreamingRecognitionConfig(config=config)
    #
    # # partial_result = types.StreamingRecognitionResult()
    #
    # # streaming_recognize returns a generator.
    # responses = client.streaming_recognize(streaming_config, requests)
    #
    # for response in responses:
    #     # Once the transcription has settled, the first result will contain the
    #     # is_final result. The other results will be for subsequent portions of
    #     # the audio.
    #     for result in response.results:
    #         print('Finished: {}'.format(result.is_final))
    #         print('Stability: {}'.format(result.stability))
    #         alternatives = result.alternatives
    #         # The alternatives are ordered from most likely to least.
    #         for alternative in alternatives:
    #             print('Confidence: {}'.format(alternative.confidence))
    #             print(u'Transcript: {}'.format(alternative.transcript))
    #             return alternative.transcript

                # for word_info in alternative.words:
                #     word = word_info.word
                #     start_time = word_info.start_time
                #     end_time = word_info.end_time
                #     print('Word: {}, start_time: {}, end_time: {}'.format(
                #         word,
                #         start_time.seconds + start_time.nanos * 1e-9,
                #         end_time.seconds + end_time.nanos * 1e-9))



actual = speech_to_text('correct.wav')
test = speech_to_text('wrong.wav')

print(find_error(actual, test, ["sh", "se"]))
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


# """Transcribe the given audio file."""
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

# client = speech.SpeechClient()
#
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'audio_files',
#     speech_file)
#
# with io.open(file_name, 'rb') as audio_file:
#     content = audio_file.read()
#
# audio = types.RecognitionAudio(content=content)
# config = types.RecognitionConfig(
#     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code='en-US')
#
# response = client.recognize(config, audio)
# # Each result is for a consecutive portion of the audio. Iterate through
# # them to get the transcripts for the entire audio file.
# for result in response.results:
#     # The first alternative is the most likely one for this portion.
#     print(u'Transcript: {}'.format(result.alternatives[0].transcript))


#
# # Instantiates a client
# client = speech.SpeechClient()
#
# # The name of the audio file to transcribe
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'audio_files',
#     speech_file)
#
# # Loads the audio into memory
# with io.open(file_name, 'rb') as audio_file:
#     content = audio_file.read()
#
# # In practice, stream should be a generator yielding chunks of audio data.
# stream = [content]
# requests = (types.StreamingRecognizeRequest(audio_content=chunk)
#             for chunk in stream)
#
# config = types.RecognitionConfig(
#     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=18000,
#     language_code='en-US'
#     # speech_contexts=[speech.types.SpeechContext(
#     #     phrases=["sheshells by the sheshore"],
#     # )]
# )
# #   speech_contexts=phrase_hints)
# streaming_config = types.StreamingRecognitionConfig(config=config,
#                                                     interim_results=True)
#
# # partial_result = types.StreamingRecognitionResult()
#
# # streaming_recognize returns a generator.
# responses = client.streaming_recognize(streaming_config, requests)