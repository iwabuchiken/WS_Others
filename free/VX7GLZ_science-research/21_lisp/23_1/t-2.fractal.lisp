(terpri t)
;;;;;;;;;;;; TINK-2 &key ;;;;;;;;;
(print ";;;;;;;;;;;; TINK-2 &key ;;;;;;;;;;;;")
(terpri t)

;; ref http://www.geocities.jp/m_hiroi/xyzzy_lisp/abclisp06.html "&key �Ŏw�肳�ꂽ����"
; &key �̎g�p��
(write
 ((lambda (a &key b c) (list a b c));lambda
 10);=> (10 NIL NIL)
)

(terpri t)
; �f�t�H���g�l�̎w��
(write
 (
  (lambda (a &key (b 1) (c 2)); param
     (list a b c); operation
     );lambda
  10 :c 22   ;=> (10 1 22)
;  10   ;=> (10 1 2)
;  10 :c 20 :b 30 ;args   ;=> (10 30 20)
  );(
);write


;============ EOF ============
