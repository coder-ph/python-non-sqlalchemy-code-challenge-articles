class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string")
        
        if hasattr(self, '_name'):
            raise AttributeError("Name should not change after the author is instantiated")
        self._name = name
        
        self._articles = []

    @property
    def name(self):
        return self._name
    
    property
    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
         
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
    
        article = Article(self, magazine, title)
        
        self._articles.append(article)
          
        magazine._articles.append(article)
        return article
        

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    all = []
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string with 2-16 characters")
        self.name = name
        
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Category must be a non-empty string")
        self.category = category
        
        self._articles = []
        
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string with 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Category must be a non-empty string")
        
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        
        return contributing_authors if contributing_authors else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all:  
            return None
        
        magazines_with_articles = [magazine for magazine in cls.all if magazine.articles()]
        if not magazines_with_articles: 
            return None
        
        top_magazine = max(magazines_with_articles, key=lambda magazine: len(magazine.articles()))
        return top_magazine


class Article:
    all = []
    def __init__(self, author, magazine, title):
    
        self.author = author
        self.magazine = magazine
        self._title = title
        
        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after instantiation")
        
        if hasattr(self, '_title') or not (5 <= len(title) <= 50):
            raise AttributeError ('cannot be changed after instantiated')
        self._title = title  