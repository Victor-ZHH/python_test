import xml.etree.ElementTree as ET

class ParseXml:
    '''
    以javapom文件为例，解析xml文件，返回依赖树
    '''

    def __init__(self):
        self.modules = []

    @staticmethod
    def parse_module_artifact_id(pom_path, is_root=False):
        tree = ET.parse(pom_path)

        root = tree.getroot()
        module = PublishModule(children=[])

        for child in root:
            if child.tag.endswith('artifactId'):
                module.artifact_id = child.text
            if child.tag.endswith('version'):
                module.version = child.text
            if child.tag.endswith('modules'):
                modules = [c.text for c in child if c.tag.endswith('module')]
                module.children = modules
        module.module_name = module.artifact_id if is_root else pom_path.split(
            '/')[-2]
        return module.module_name, module

    def __parse_children(self, new_dir):
        pom = os.path.realpath(os.path.join(new_dir, 'pom.xml'))
        _, module = self.parse_module_artifact_id(pom, False)
        self.modules.append(module)

        for c in module.children:
            new_path = os.path.join(new_dir, c)
            self.__parse_children(new_path)

    def get_modules_info(self, repo_dir):
        root_pom = os.path.realpath(os.path.join(repo_dir, 'pom.xml'))
        root, root_module = self.parse_module_artifact_id(root_pom, True)

        children = root_module.children
        self.modules.append(root_module)
        for module_name in children:
            self.__parse_children(os.path.join(repo_dir, module_name))
        return root, self.modules
