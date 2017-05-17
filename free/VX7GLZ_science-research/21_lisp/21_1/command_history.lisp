(setq fpath "out.data")

;ref https://www.tutorialspoint.com/lisp/lisp_file_io.htm
(with-open-file (stream fpath :direction :output)
  (format stream "The options are same as the keyword arguments to the function open.")
  (format t "file opened : ~a" fpath)
  (terpri stream))
(print "file closed")


      