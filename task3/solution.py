import random
import yaml
from abc import ABC


# Levels = yaml.load(
# '''
# levels:
#     - !easy_level {}
#     - !medium_level
#         enemy: ['rat']
#     - !hard_level
#         enemy:
#             - rat
#             - snake
#             - dragon
#         enemy_count: 10
# ''')


class AbstractLevel(yaml.YAMLObject):

    @classmethod
    def get_map(cls):
        return cls.Map()

    @classmethod
    def get_objects(cls):
        return cls.Objects()

    class Map(ABC):
        pass

    class Objects(ABC):
        pass


class EasyLevel(AbstractLevel):
    yaml_tag = u'!easy_level'

    @classmethod
    def from_yaml(Class, loader, node):
        # def get_levels(loader, node):
        #     data = loader.construct_mapping(node)
        #     rep = Class.make_report(data["title"])
        #     rep.filename = data["filename"]
        #     # на данный момент data["parts"] пуст. Он будет заполнен позже, соответствующим обработчиком,
        #     # сохраняем на него ссылку, дополнив сразу частями из rep.parts
        #     data["parts"].extend(rep.parts)
        #     rep.parts = data["parts"]
        #     return rep

        #
        # # обработчик создания части !chapter
        # def get_chapter(loader, node):
        #     data = loader.construct_mapping(node)
        #     ch = Class.make_chapter(data["caption"])
        #     # аналогично предыдущему обработчику
        #     data["parts"].extend(ch.objects)
        #     ch.objects = data["parts"]
        #     return ch
        #
        # # обработчик создания ссылки !link
        # def get_link(loader, node):
        #     data = loader.construct_mapping(node)
        #     lnk = Class.make_link(data["obj"], data["href"])
        #     return lnk
        #
        # # обработчик создания изображения !img
        # def get_img(loader, node):
        #     data = loader.construct_mapping(node)
        #     img = Class.make_img(data["alt_text"], data["src"])
        #     return img

        # добавляем обработчики
        # loader.add_constructor(u"!easy_level", get_report)
        # loader.add_constructor(u"!chapter", get_chapter)
        # loader.add_constructor(u"!link", get_link)
        # loader.add_constructor(u"!img", get_img)

        # возвращаем результат yaml обработчика - отчёт
        data = loader.construct_mapping(node)
        data['map'] = Class.get_map()
        data['obj'] = Class.get_objects()
        return data

    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(5)] for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    if i == 0 or j == 0 or i == 4 or j == 4:
                        self.Map[j][i] = -1  # граница карты
                    else:
                        self.Map[j][i] = random.randint(0, 2)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (2, 2))]
            self.config = {}

        def get_objects(self, _map):
            for obj_name in ['rat']:
                coord = (random.randint(1, 3), random.randint(1, 3))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 3), random.randint(1, 3))

                self.objects.append((obj_name, coord))

            return self.objects


class MediumLevel(AbstractLevel):
    yaml_tag = u'!medium_level'

    @classmethod
    def from_yaml(Class, loader, node):
        # def get_enemy(loader, node):
        #     data = loader.construct_mapping(node)
        #     data['obj'] = Class.get_objects()
        #     rep = Class.make_report(data["title"])
        #     rep.filename = data["filename"]
        #     # на данный момент data["parts"] пуст. Он будет заполнен позже, соответствующим обработчиком,
        #     # сохраняем на него ссылку, дополнив сразу частями из rep.parts
        #     data["parts"].extend(rep.parts)
        #     rep.parts = data["parts"]
        #     return rep

        #
        # # обработчик создания части !chapter
        # def get_chapter(loader, node):
        #     data = loader.construct_mapping(node)
        #     ch = Class.make_chapter(data["caption"])
        #     # аналогично предыдущему обработчику
        #     data["parts"].extend(ch.objects)
        #     ch.objects = data["parts"]
        #     return ch
        #
        # # обработчик создания ссылки !link
        # def get_link(loader, node):
        #     data = loader.construct_mapping(node)
        #     lnk = Class.make_link(data["obj"], data["href"])
        #     return lnk
        #
        # # обработчик создания изображения !img
        # def get_img(loader, node):
        #     data = loader.construct_mapping(node)
        #     img = Class.make_img(data["alt_text"], data["src"])
        #     return img

        # добавляем обработчики
        #loader.add_constructor(u"enemy", get_enemy)
        # loader.add_constructor(u"!chapter", get_chapter)
        # loader.add_constructor(u"!link", get_link)
        # loader.add_constructor(u"!img", get_img)

        # возвращаем результат yaml обработчика - отчёт
        data = loader.construct_mapping(node)
        data['map'] = Class.get_map()
        _obj = Class.get_objects()
        #_obj.config['enemy'].extend(data['enemy'])

        data['obj'] = _obj
        data['obj'].config['enemy'].extend(_obj.config['enemy'])
        _obj.config['enemy'] = data['enemy']
        return data

    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(8)] for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    if i == 0 or j == 0 or i == 7 or j == 7:
                        self.Map[j][i] = -1  # граница карты
                    else:
                        self.Map[j][i] = random.randint(0, 2)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (4, 4))]
            self.config = {'enemy': []}

        def get_objects(self, _map):
            for obj_name in self.config['enemy']:
                coord = (random.randint(1, 6), random.randint(1, 6))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 6), random.randint(1, 6))

                self.objects.append((obj_name, coord))

            return self.objects


class HardLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(10)] for _ in range(10)]
            for i in range(10):
                for j in range(10):
                    if i == 0 or j == 0 or i == 9 or j == 9:
                        self.Map[j][i] = -1  # граница карты :: непроходимый участок карты
                    else:
                        self.Map[j][i] = random.randint(-1, 8)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (5, 5))]
            self.config = {'enemy_count': 5, 'enemy': []}

        def get_objects(self, _map):
            for obj_name in self.config['enemy']:
                for tmp_int in range(self.config['enemy_count']):
                    coord = (random.randint(1, 8), random.randint(1, 8))
                    intersect = True
                    while intersect:
                        intersect = False
                        if _map[coord[0]][coord[1]] == -1:
                            intersect = True
                            coord = (random.randint(1, 8), random.randint(1, 8))
                            continue
                        for obj in self.objects:
                            if coord == obj[1]:
                                intersect = True
                                coord = (random.randint(1, 8), random.randint(1, 8))

                    self.objects.append((obj_name, coord))

            return self.objects


Levels = '''
levels:
    - !easy_level {}
    - !medium_level
         enemy: ['rat']
'''
levels_result = yaml.load(Levels)
print(levels_result)

Levels = {'levels':[]}
_map = EasyLevel.Map()
_obj = EasyLevel.Objects()
Levels['levels'].append({'map': _map, 'obj': _obj})

_map = MediumLevel.Map()
_obj = MediumLevel.Objects()
_obj.config = {'enemy':['rat']}
Levels['levels'].append({'map': _map, 'obj': _obj})

print(Levels)
#
# _map = HardLevel.Map()
# _obj = HardLevel.Objects()
# _obj.config = {'enemy': ['rat', 'snake', 'dragon'], 'enemy_count': 10}
# Levels['levels'].append({'map': _map, 'obj': _obj})