from pdf2zh import translate, translate_stream

params = {"lang_in": "en", "lang_out": "vn", "service": "google", "thread": 4}
file_mono, file_dual = translate(files=["/mnt/e/PDFMathTranslate/pdf2zh_files/facenet.pdf"], **params)[0]
with open("/mnt/e/PDFMathTranslate/pdf2zh_files/facenet.pdf", "rb") as f:
    stream_mono, stream_dual = translate_stream(stream=f.read(), **params)