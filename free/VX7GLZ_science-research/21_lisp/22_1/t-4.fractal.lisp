(setq L1 '(1 2 3 4 5))

(setq L2 '(6 7 8 9 10))

(write-line "L1")

(print L1)				; (1 2 3 4 5)

(mapcar #'+ L1 L2)

(setq res (mapcar #'+ L1 L2))

(print res)				;(7 9 11 13 15)





