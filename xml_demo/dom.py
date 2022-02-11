'''
xml即可扩展标记语言，它可以用来标记数据、定义数据类型，是一种允许用户对自己的标记语言进行定义的源语言。
特征：
  它是有标签对组成，<aa></aa>
  标签可以有属性：<aa id='123'></aa>
  标签对可以嵌入数据：<aa>abc</aa>
  标签可以嵌入子标签（具有层级关系）
'''

from xml.dom.minidom import parse, Document, parseString, Element

class ParseXml:
    '''
    xml 文件操作
    '''  

	def parse_xml(self, repo_dir, file_name):
		'''
		return: xml文档对象
		'''
        pom_path = os.path.join(repo_dir, file_name)
        dom_tree = parse(pom_path)
        collection = dom_tree.documentElement
		return dom_tree, collection

	def get_xml_ele_by_tag_name(self, tag_name):
		ele = collection.getElementsByTagName(tag_name) # NodeList 找不到的时候为空
		# 获取数据 <a>test</a>
		if ele:
			data = ele[0].firstChild.data.strip() # test
			return data
		return

	def get_node_list(self, node):
		# 返回node的直接子节点列表
		return node.childNodes

	def modify_ele_text(self, tag_name, new_data):
		ele = collection.getElementsByTagName(tag_name)
		if ele:
			ele[0].firstChild.data = new_data
	
	def make_node(tag_name: str, text: str):
		dom = Document()
		node = dom.createElement(tag_name) # Element
		# 如果子元素为文本对象
		text = dom.createTextNode(text)
		node.appendChild(text)
		# 如果子元素为节点, 重复创建节点
		# child = dom.createElement(child_tag_name)
        # node.appendChild(child)

	def update_xml(self, dom_tree, file_path):
		# file_path 文件的绝对路径
		# dom_tree parse 返回的xml对象
		with open(file_path, "w") as f:
			dom_tree.writexml(f)


