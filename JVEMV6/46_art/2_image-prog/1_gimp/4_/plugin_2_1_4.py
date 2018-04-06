#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	file	: C:\WORKS_2\WS\WS_Others\JVEMV6\46_art\2_image-prog\1_gimp\4_\plugin_2_1_4.py

	at		: 2018/04/06 14:34:49

	plugin at : C:\WORKS_2\Programs\GIMP 2\plugins

'''

from gimpfu import *
########################################################################
class ImageObject :
	
	image = None
	layer = None
	
	def __init__( self, image ):
		self.image = image
		
		return
		
	def get_Image(self):
		
		return self.image
	
	def add_Layer(self, layer_Name):
		
		width   = self.image.width
		height  = self.image.height
		type    = RGB_IMAGE
		opacity = 100
		mode    = NORMAL_MODE

		self.layer = gimp.Layer(image, name, width, height, type, opacity, mode)
		
  		self.layer.fill(1)
  #
		# 画像データの 0 番目の位置にレイヤーを挿入する
		position = 0
		self.image.add_layer(layer, position)
		
	def get_Layer(self):
		
		if self.layer == None :
			
			pdb.gimp_message("layer ==> None !!!")
			
			return False
		
		# return layer
		return self.layer

def create_image(width, height):
	# 画像データを生成
	return gimp.Image(width, height, RGB)

def display_image(image):
	gimp.Display(image)

def add_layer(image, name):
  # レイヤーの作成に必要なパラメータ
  width   = image.width
  height  = image.height
  type    = RGB_IMAGE
  opacity = 100
  mode    = NORMAL_MODE
  #
  # パラメータをもとにレイヤーを作成
  layer = gimp.Layer(image, name, width, height, type, opacity, mode)
  #
  # レイヤーを背景色で塗りつぶす（GIMP のデフォルトの挙動に合わせています）
  layer.fill(1)
  #
  # 画像データの 0 番目の位置にレイヤーを挿入する
  position = 0
  image.add_layer(layer, position)
  #
  return layer

def draw_pencil_lines(drawable, lines):
  # ペンシルツールで線を描画する
  pdb.gimp_pencil(drawable, len(lines), lines)
  
def draw_rect(drawable, x1, y1, x2, y2):
  lines = [x1, y1, x2, y1, x2, y2, x1, y2, x1, y1]
  draw_pencil_lines(drawable, lines)

def test_2(timg, tdrawable):
	
	image = create_image(640, 400)
	
	name_Layer = "L-1"
	
	# image instance
	imageObj = ImageObject( image )

	im = imageObj.get_Image()
	
# 	im.add_Layer(name_Layer)
# 	
# 	#debug
# 	pdb.gimp_message("layer => added")
# 	
# 	layer = im.get_Layer()
# 
# 	draw_rect(layer, 190, 210, 490, 310)
# # 	draw_rect(layer, 390, 210, 490, 310)
	
	display_image(im)
# 	display_image(image)

def test_1(timg, tdrawable):
	
	image = create_image(640, 400)
	
	name_Layer = "L-1"
	
	layer = add_layer(image, name_Layer)
# 	layer = add_layer(image, "背景")

	draw_rect(layer, 390, 210, 490, 310)
	
	display_image(image)


def plugin_main(timg, tdrawable):
	
	test_2(timg, tdrawable)
# 	test_1(timg, tdrawable)
	
# 	image = create_image(640, 400)
# 	
# 	name_Layer = "L-1"
# 	
# 	layer = add_layer(image, name_Layer)
# # 	layer = add_layer(image, "背景")
# 
# 	draw_rect(layer, 390, 210, 490, 310)
# 	
# 	display_image(image)

########################################################################



register(
	'plugin_main',			# プロシジャの名前
	'転写スクリプト。アクティブなレイヤーの内容を、下にあるレイヤーに転写する。',
	# プロシジャの説明文
	'ver 2.8 以上を対象とした転写スクリプト。転写元のレイヤーから転写先のレイヤーへ内容を転写する。レイヤーグループ内での動作や、レイヤーマスクの保持が行われる。',
	# PDBに登録する追加情報
	'かんら・から',					# 作者名
	'GPLv3',					# ライセンス情報
	'2012.12.15',					# 作成日
	'new image',				# メニューアイテム
	'*',						# 対応する画像タイプ

	[
		(PF_IMAGE, 'image', 'Input image', None),
		(PF_DRAWABLE, 'drawable', 'Input drawable', None)
	],	# プロシジャの引数
	[],	# 戻り値の定義

	plugin_main,			# 処理を埋け持つ関数名
	menu='<Image>/Layer/user_libs'	# メニュー表示場所
	)


main() # プラグインを駆動させるための関数

