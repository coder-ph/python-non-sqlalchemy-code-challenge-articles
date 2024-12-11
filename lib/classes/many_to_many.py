class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all.append(self)
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError (
                'author must be an instance of Author'
            )
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError (
                'magazine must be an instance of Author'
            )
            
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, 'title'):
            raise ValueError ('name cannot be changed after instantiated')
        
        if not isinstance(title, str) and 5 <= len(title) <= 50:
            raise ValueError ('Title must be between 5 to 50 characters')
            
        else:
            self._title = title
        
class Author:
    def __init__(self, name):
        self.name = name
        self.author_articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise ValueError ('name must not be changed after instantiation')
        if not isinstance(name, str) and not len(name) >0:
            raise ValueError ('Name must be more than 0 characters')
        self._name = name
        
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError('magazine must be an instance of Magazine')
        
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError('Title must be a string and between 5 to 50 characters')
        
        article = Article(self, magazine, title)
        self.author_articles.append(article)
        
        return article

    def topic_areas(self):
        if self.author_articles:
            return list(set(magazine.category for magazine in self.magazines()))
        else:
            return None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.myarticles = []
        
        self.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2<= len(name)<= 16:
            self._name = name
        else:
            raise ValueError('Nam must be a string')
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) >0:
            self._category = category
        else:
            raise ValueError (
                'Category must be a string'
            )
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        articles = self.articles()
        if articles:
            return [article.title for article in articles]
        else:
            return None

    def contributing_authors(self):
        constributing_authors = []
        for author in self.contributors():
            article_count = len([article for article in  Article.all if article.author == author and article.magazine == self])
            if article_count >2:
                constributing_authors.append(author)
        if constributing_authors:
            return constributing_authors
        else:
            return None
        
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        
        magazines_with_articles = [magazine for magazine in cls.all if magazine.articles()]
        if not magazines_with_articles: 
            return None
        
        top_magazine = max(magazines_with_articles, key=lambda magazine: len(magazine.articles()))
        return top_magazine