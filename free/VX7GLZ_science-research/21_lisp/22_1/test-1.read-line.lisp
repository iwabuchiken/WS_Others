;; pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\21_lisp\22_1
;; test-1.lisp
(print "yes")

(setq fname "data-1.dat")

(setq fpath_dst "C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/21_lisp/22_1/data-1.dat")

;(setq f (in (open fpath_dst :if-does-not-exist nil)))
(setq in (open fpath_dst :if-does-not-exist nil))
;(let f (in (open fpath_dst :if-does-not-exist nil)))

(print in)
(setq count 1)
(loop for line = (read-line in nil)
     while line
     do (format t "(~d) '~a'" count line)
        (terpri t)
        ;(+ count 1)
        (setq count (+ count 1))
     )
(close in)
