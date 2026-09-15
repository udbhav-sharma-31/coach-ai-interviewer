import json
import os
import random
from backend.evaluation.additional_questions import QUESTIONS as ADDITIONAL_QUESTIONS

OUTPUT_PATH = "data/interview_answers.json"


QUESTIONS = [

    # ============================================================
    # PYTHON — 10 QUESTIONS
    # ============================================================

    {
        "question": "What is the difference between a list and a tuple in Python?",
        "topic": "python",
        "concepts": ["list", "tuple", "mutability"],
        "incorrect": [
            "A list stores numbers while a tuple stores strings.",
            "A tuple is used for functions and a list is used for classes.",
            "Lists can only contain one type of data.",
            "There is no difference between a list and a tuple."
        ],
        "weak": [
            "Lists and tuples are both collections, but they are used differently.",
            "A list can be changed while a tuple is more fixed.",
            "Lists and tuples both store multiple values.",
            "A tuple is generally not changed after it is created."
        ],
        "partial": [
            "A list is mutable, so its elements can be changed, while a tuple is immutable.",
            "Both can hold multiple values, but lists support modification whereas tuples generally do not.",
            "The main difference is mutability: lists can be modified after creation and tuples cannot.",
            "Tuples provide an immutable sequence, while lists provide a mutable sequence."
        ],
        "good": [
            "Lists and tuples are both ordered sequences, but lists are mutable and tuples are immutable. This makes tuples useful when the collection should not change.",
            "A list allows operations such as append, remove, and item assignment, whereas a tuple cannot normally be modified after creation.",
            "The important distinction is mutability. Lists can have their contents changed, while tuples are fixed after construction and can sometimes be used as dictionary keys.",
            "Both support indexing and iteration, but a tuple represents an immutable sequence while a list represents a mutable one."
        ],
        "excellent": [
            "Both are ordered sequence types, but a list is mutable and a tuple is immutable. This affects what operations are allowed and whether the object can be safely used as an immutable value. A tuple containing only hashable elements can also be used as a dictionary key.",
            "Lists and tuples both support indexing, slicing, and iteration. The key semantic difference is mutability: list elements can be added, removed, or reassigned, while tuple contents cannot be changed after creation.",
            "A list is appropriate when a collection needs to change during program execution. A tuple is useful for fixed records or immutable sequences. Tuples can also be more suitable when the values should communicate that they are not intended to change.",
            "The distinction is not simply performance. Lists provide mutable sequence behavior, while tuples provide immutable sequence behavior. That immutability can make tuples useful for fixed data and, when their elements are hashable, for dictionary keys or set members."
        ]
    },

    {
        "question": "What is a dictionary in Python?",
        "topic": "python",
        "concepts": ["dictionary", "key-value", "mapping"],
        "incorrect": [
            "A dictionary is a Python file containing functions.",
            "A dictionary stores values only by their position.",
            "A dictionary can contain only text.",
            "A dictionary is another name for a list."
        ],
        "weak": [
            "A dictionary stores information using keys and values.",
            "It is a collection where values are associated with keys.",
            "Dictionaries are useful for storing related information.",
            "You can use a key to get a value from a dictionary."
        ],
        "partial": [
            "A dictionary is a collection of key-value pairs.",
            "Dictionaries map keys to values and allow values to be retrieved using their keys.",
            "A dictionary stores data in a mapping rather than relying only on numeric indexes.",
            "Keys identify values in a dictionary, such as using a name to find a person's age."
        ],
        "good": [
            "A Python dictionary stores key-value pairs. Keys are used to look up their corresponding values efficiently.",
            "Dictionaries implement a mapping between keys and values. For example, a student's name could be a key and their marks could be the associated value.",
            "A dictionary is useful when data should be accessed using meaningful keys instead of positions. Keys must be hashable.",
            "Dictionaries provide operations for inserting, updating, deleting, and retrieving values associated with keys."
        ],
        "excellent": [
            "A dictionary is Python's built-in mapping type. It associates hashable keys with values and provides efficient average-case lookup, insertion, and deletion. Unlike a list, access is conceptually based on keys rather than integer positions.",
            "Dictionaries are useful for representing structured relationships such as user IDs to records. Keys must be hashable, while values can generally be any Python object. Assigning an existing key updates its value.",
            "A dictionary uses a hash-table-based mapping implementation. Its keys uniquely identify entries, and modern Python dictionaries preserve insertion order as part of their language behavior, although ordering is separate from the purpose of key-based lookup.",
            "For example, `{\"name\": \"A\", \"age\": 20}` maps the key `name` to `A` and `age` to `20`. Dictionary operations include lookup with a key, insertion, updating, deletion, and iteration over keys, values, or key-value pairs."
        ]
    },

    {
        "question": "What is a Python function?",
        "topic": "python",
        "concepts": ["function", "def", "parameters"],
        "incorrect": [
            "A function is a variable that stores only numbers.",
            "A function is a type of Python loop.",
            "A function automatically runs every program.",
            "A function is used only for printing."
        ],
        "weak": [
            "A function is a block of code that performs a task.",
            "Functions help organize Python code.",
            "A function can be called when we need it.",
            "Functions can accept inputs and produce outputs."
        ],
        "partial": [
            "A function is a reusable block of code defined with `def`.",
            "Functions can take parameters and return a result.",
            "A function groups instructions so they can be called multiple times.",
            "Functions reduce repeated code by putting related operations in one place."
        ],
        "good": [
            "A Python function is a reusable block of code defined using `def`. It can accept parameters, perform operations, and optionally return a value.",
            "Functions improve code organization by encapsulating a particular task. The function body executes when the function is called.",
            "A function can receive input through parameters and send a result back using `return`. It can then be reused from different parts of a program.",
            "Using functions makes programs easier to maintain because common logic can be defined once and called whenever needed."
        ],
        "excellent": [
            "A function encapsulates reusable behavior. It is defined with `def`, can have parameters with optional default values, and can return a value. Python also supports positional arguments, keyword arguments, variable-length arguments, and higher-order use of functions.",
            "Functions provide abstraction and reuse. The caller does not need to know the internal implementation; it supplies the required arguments and receives the function's result. Local variables created inside a function normally belong to that function's scope.",
            "A function is an executable object in Python, not merely a code block. Defining it creates a function object, while calling it executes its body with a new local execution context. A `return` statement ends the call and optionally supplies a result.",
            "Good function design usually gives one clear responsibility, uses meaningful parameters, and avoids unnecessary side effects. Functions are fundamental to decomposition, testing, reuse, and abstraction in Python programs."
        ]
    },

    {
        "question": "What is inheritance in Python?",
        "topic": "python",
        "concepts": ["inheritance", "class", "object-oriented-programming"],
        "incorrect": [
            "Inheritance means copying a Python file.",
            "Inheritance is used to create variables automatically.",
            "Inheritance means one function calls another function.",
            "Inheritance is only related to database tables."
        ],
        "weak": [
            "Inheritance allows one class to use another class.",
            "A child class can get features from a parent class.",
            "It is an object-oriented programming concept.",
            "Inheritance helps reuse class functionality."
        ],
        "partial": [
            "Inheritance allows a child class to inherit attributes and methods from a parent class.",
            "A derived class can extend or override behavior provided by a base class.",
            "Python classes can inherit from one or more other classes.",
            "Inheritance allows related classes to share common behavior."
        ],
        "good": [
            "Inheritance allows a class to derive behavior and attributes from another class. The derived class can add new behavior or override inherited methods.",
            "In Python, a child class can inherit from a parent class using class syntax. Methods can be reused or customized in the child.",
            "Inheritance supports code reuse and models an is-a relationship between classes. Python also supports multiple inheritance.",
            "A subclass can call inherited methods directly or use `super()` to access behavior from a parent implementation."
        ],
        "excellent": [
            "Inheritance creates a relationship in which a subclass derives behavior from one or more base classes. Python resolves attribute and method lookup through the method resolution order, or MRO, which is especially important with multiple inheritance.",
            "A subclass inherits accessible attributes and methods from its base classes but can override them to provide specialized behavior. `super()` is commonly used to cooperate with the parent implementation rather than directly naming a specific base class.",
            "Inheritance is useful for representing an is-a relationship and sharing common behavior, but composition can sometimes be preferable when objects should contain or delegate to other objects rather than specialize them.",
            "Python supports single and multiple inheritance. With multiple inheritance, the C3 linearization algorithm determines the MRO, allowing Python to resolve methods consistently while respecting the inheritance hierarchy."
        ]
    },

    {
        "question": "What is exception handling in Python?",
        "topic": "python",
        "concepts": ["exceptions", "try", "except"],
        "incorrect": [
            "Exception handling removes all errors from a program.",
            "Exceptions are only used to print messages.",
            "Python exceptions are handled using loops only.",
            "An exception means the computer has permanently failed."
        ],
        "weak": [
            "Exception handling deals with errors in Python.",
            "Python uses try and except for handling errors.",
            "It prevents some errors from stopping the program.",
            "Exceptions can be caught by the program."
        ],
        "partial": [
            "Exception handling uses `try` and `except` to respond to runtime errors.",
            "Code that may raise an exception can be placed inside a `try` block.",
            "An `except` block specifies what should happen for a particular exception.",
            "Python also provides `finally` for cleanup that should happen whether an exception occurs or not."
        ],
        "good": [
            "Python exception handling uses `try`, `except`, `else`, and `finally` blocks to handle exceptional situations.",
            "A `try` block contains code that may fail, while `except` handles specified exceptions. `finally` is useful for cleanup operations.",
            "Handling exceptions allows a program to respond to expected runtime problems instead of terminating unexpectedly.",
            "Specific exception types should generally be caught so that unrelated programming errors are not accidentally hidden."
        ],
        "excellent": [
            "Exception handling separates normal program flow from exceptional conditions. Code that may raise an exception is placed in `try`, matching `except` clauses handle particular exception types, `else` runs when no exception occurs, and `finally` runs for cleanup regardless of success or failure.",
            "Good exception handling is selective rather than using a broad `except` indiscriminately. Catching specific exceptions makes failures easier to diagnose and prevents programming bugs from being silently hidden.",
            "Python exceptions propagate up the call stack until a compatible handler is found. If no handler catches the exception, the program terminates with a traceback. Exceptions can also be deliberately raised using `raise`.",
            "Exception handling is particularly useful around operations such as file access, network requests, parsing, and external services. Cleanup resources should often be handled with `finally` or context managers such as `with`."
        ]
    },

    {
        "question": "What is a Python class?",
        "topic": "python",
        "concepts": ["class", "object", "oop"],
        "incorrect": [
            "A class is only a collection of numbers.",
            "A class is the same thing as a Python loop.",
            "A class can contain only functions.",
            "A class is used only to create files."
        ],
        "weak": [
            "A class is a blueprint for objects.",
            "Classes are used in object-oriented programming.",
            "An object can be created from a class.",
            "A class can contain data and methods."
        ],
        "partial": [
            "A class defines attributes and methods that objects created from it can use.",
            "A class acts as a blueprint while an object is an instance of that class.",
            "Classes allow related data and behavior to be grouped together.",
            "Python classes can define methods, attributes, constructors, and other behavior."
        ],
        "good": [
            "A class defines the structure and behavior of objects. Instances created from the class can have attributes and use its methods.",
            "Classes support object-oriented programming by combining data and behavior into a reusable definition.",
            "The `__init__` method is commonly used to initialize instance attributes when an object is created.",
            "A class can define instance methods, class methods, static methods, properties, and other attributes."
        ],
        "excellent": [
            "A Python class is a user-defined type that combines state and behavior. Creating an instance produces an object whose attributes represent state and whose methods implement behavior. Python's object model treats classes themselves as objects too.",
            "The `self` parameter conventionally refers to the current instance when an instance method is called. `__init__` initializes an already-created instance rather than technically constructing the object itself; object creation involves `__new__` as well.",
            "Classes support encapsulation, inheritance, polymorphism, and abstraction, although Python implements these concepts more flexibly than languages with strict access modifiers.",
            "A class can define instance-level data, class-level data, methods, properties, and special methods such as `__str__` or `__len__`. Instances can also have dynamically added attributes depending on the class design."
        ]
    },

    {
        "question": "What is a Python decorator?",
        "topic": "python",
        "concepts": ["decorator", "function", "higher-order-function"],
        "incorrect": [
            "A decorator changes the color of Python code.",
            "A decorator is a special kind of loop.",
            "Decorators are used only with classes.",
            "A decorator automatically fixes syntax errors."
        ],
        "weak": [
            "A decorator adds something to a function.",
            "It is written using the `@` symbol.",
            "Decorators can modify function behavior.",
            "They are commonly used with functions."
        ],
        "partial": [
            "A decorator is a callable that takes a function and returns a modified or wrapped function.",
            "The `@decorator` syntax applies a decorator to the following function or class.",
            "Decorators allow behavior to be added without changing the original function body.",
            "Logging and authentication are examples of functionality that can be implemented with decorators."
        ],
        "good": [
            "A decorator wraps or transforms a function or class to add behavior. Python provides the `@name` syntax as convenient syntax for applying one.",
            "A decorator is based on Python's ability to treat functions as objects. It can accept a function, define additional behavior, and return a callable.",
            "Decorators are useful for cross-cutting concerns such as logging, authorization, timing, caching, and validation.",
            "A wrapper created by a decorator often calls the original function before or after performing additional work."
        ],
        "excellent": [
            "A decorator is a higher-order callable that receives a function or class and returns a replacement callable, allowing behavior to be composed around the original object. `@decorator` is syntactic sugar for rebinding the decorated name.",
            "Decorators are valuable when the same behavior must be applied consistently across many functions. `functools.wraps` is commonly used on wrapper functions so metadata such as the original name and documentation is preserved.",
            "A decorator can intercept arguments and return values, perform work before or after the wrapped call, or even choose not to call the original function. This makes decorators useful for logging, caching, access control, and instrumentation.",
            "Because decoration happens when the function definition is executed, the decorator expression is evaluated and applied at definition time. This is different from the wrapper's actual function-call execution, which happens later."
        ]
    },

    {
        "question": "What is the difference between shallow copy and deep copy in Python?",
        "topic": "python",
        "concepts": ["copy", "deepcopy", "references"],
        "incorrect": [
            "A shallow copy always duplicates every nested object.",
            "A deep copy only copies numbers.",
            "Both copies always behave exactly the same.",
            "Deep copy means copying only the first level."
        ],
        "weak": [
            "Shallow copy copies less than deep copy.",
            "Deep copy makes a more complete copy.",
            "Nested objects are important when comparing the two.",
            "Python provides copy functions for both operations."
        ],
        "partial": [
            "A shallow copy creates a new outer object but keeps references to nested objects.",
            "A deep copy recursively copies nested objects as well.",
            "Changing a nested mutable object can affect both structures after a shallow copy.",
            "The `copy` module provides `copy()` and `deepcopy()`."
        ],
        "good": [
            "A shallow copy duplicates the outer container but its nested objects are still shared. A deep copy recursively creates independent copies of nested objects.",
            "If a list contains another mutable list, a shallow copy creates a new outer list while both lists may reference the same inner list.",
            "Deep copying is useful when nested mutable state must be independent, although it can be more expensive and may have limitations with certain objects.",
            "Python's `copy.copy()` performs a shallow copy and `copy.deepcopy()` recursively copies supported nested objects."
        ],
        "excellent": [
            "The distinction is about object references. A shallow copy creates a new top-level object while retaining references to contained objects; a deep copy recursively copies objects so nested mutable state is generally independent.",
            "For example, copying `[[1, 2], [3, 4]]` shallowly creates a new outer list but the inner lists remain shared. A deep copy creates new inner lists too, so mutations to the nested structure do not affect the original.",
            "Deep copying is not simply 'copy everything blindly.' Python's deepcopy mechanism maintains a memo of already-copied objects to handle shared references and cycles, and some objects require special handling or cannot be meaningfully copied.",
            "Choosing between shallow and deep copying depends on the desired ownership of mutable state. A shallow copy is often sufficient when nested objects are immutable or intentionally shared, while deep copying is useful when independent nested state is required."
        ]
    },

    {
        "question": "What is a Python generator?",
        "topic": "python",
        "concepts": ["generator", "yield", "iterator"],
        "incorrect": [
            "A generator creates random passwords automatically.",
            "A generator is a type of database.",
            "Generators store every result permanently in memory.",
            "A generator is another name for a normal variable."
        ],
        "weak": [
            "A generator produces values one at a time.",
            "Generators use `yield`.",
            "They can save memory.",
            "Generators are related to iteration."
        ],
        "partial": [
            "A generator is an iterator-producing function that uses `yield`.",
            "Instead of returning all results at once, a generator produces values lazily.",
            "Generators are useful when processing large sequences.",
            "Calling `next()` on a generator resumes execution until the next `yield`."
        ],
        "good": [
            "A generator function uses `yield` to produce values lazily. Each call to `next()` resumes the function from where it last stopped.",
            "Generators avoid storing an entire sequence in memory at once, which makes them useful for large or streaming data.",
            "A generator maintains its execution state between yields and raises `StopIteration` when it is exhausted.",
            "Generator expressions provide a compact way to create lazy sequences without immediately constructing a complete list."
        ],
        "excellent": [
            "A generator is a stateful iterator commonly created by a function containing `yield`. Calling the generator function creates a generator object without executing the entire body; execution occurs incrementally as values are requested.",
            "Generators provide lazy evaluation. They are particularly useful for large datasets, files, pipelines, and streams because only the currently needed value generally has to be produced rather than materializing the complete sequence.",
            "When a generator reaches `yield`, its local state and execution position are suspended. A later `next()` resumes from that point. When the function returns, iteration ends through `StopIteration`.",
            "Generator expressions use syntax similar to list comprehensions but produce values lazily. This can reduce memory consumption, although lazy iteration may not be appropriate when random access or repeated traversal is required."
        ]
    },

    {
        "question": "What is the difference between == and is in Python?",
        "topic": "python",
        "concepts": ["equality", "identity", "operators"],
        "incorrect": [
            "`is` compares two numbers mathematically.",
            "`==` checks whether two variables have the same memory address.",
            "Both operators always perform exactly the same operation.",
            "`is` is used only for strings."
        ],
        "weak": [
            "`==` and `is` are comparison operators.",
            "One compares values and the other checks identity.",
            "`is` is related to whether objects are the same object.",
            "`==` is usually used to compare values."
        ],
        "partial": [
            "`==` tests equality while `is` tests object identity.",
            "Two separate objects can be equal with `==` without being identical with `is`.",
            "`is` checks whether two references point to the same object.",
            "`==` generally uses an object's equality behavior, while `is` checks identity."
        ],
        "good": [
            "`==` asks whether two objects are equal in value, while `is` asks whether they are the exact same object.",
            "Two separately created lists containing the same values can return `True` for `==` but `False` for `is`.",
            "`is` is commonly appropriate for identity checks such as `x is None`, while `==` should normally be used for value comparison.",
            "Identity and equality are different concepts: identity concerns object sameness, whereas equality concerns equivalent values."
        ],
        "excellent": [
            "`==` invokes equality comparison semantics, potentially through methods such as `__eq__`, while `is` performs an identity test. Therefore two distinct objects can compare equal without being the same object.",
            "For example, two independently created lists `[1, 2]` may satisfy `a == b` but not `a is b`. The identity operator is particularly useful for singleton-like values such as `None`.",
            "Using `is` when value equality is intended can produce incorrect results because object identity is not guaranteed merely because two objects contain the same value. Conversely, `==` may invoke user-defined equality logic.",
            "The distinction is important because Python variables hold references to objects. `is` compares whether those references identify the same object, while `==` asks whether the objects are considered equal according to their equality semantics."
        ]
    },

    {
        "question": "What is a list comprehension in Python?",
        "topic": "python",
        "concepts": ["list-comprehension", "iteration", "filtering"],
        "incorrect": [
            "A list comprehension deletes a list.",
            "It can only be used with strings.",
            "A list comprehension is a database query.",
            "It creates classes automatically."
        ],
        "weak": [
            "A list comprehension is a short way to create a list.",
            "It uses a loop-like syntax inside brackets.",
            "It can transform values while creating a list.",
            "Conditions can be included in a list comprehension."
        ],
        "partial": [
            "A list comprehension creates a list from an iterable using an expression and optional condition.",
            "It can replace some simple `for` loops that build lists.",
            "For example, `[x * 2 for x in numbers]` creates a new list with doubled values.",
            "A condition can filter elements during list creation."
        ],
        "good": [
            "A list comprehension combines iteration, transformation, and optional filtering into concise syntax for constructing a list.",
            "For example, `[x * x for x in numbers if x > 0]` squares only the positive numbers.",
            "List comprehensions are often clearer than multi-line loops for simple transformations, but complicated logic may be better expressed using a normal loop.",
            "The result is a new list, unlike a generator expression which produces values lazily."
        ],
        "excellent": [
            "A list comprehension has the general form `[expression for item in iterable if condition]`. The expression determines each output value, while the optional condition determines which items are included.",
            "List comprehensions are concise but still eagerly construct the resulting list. For large or streaming data, a generator expression can provide similar transformation logic while evaluating values lazily.",
            "Nested comprehensions are possible, but excessive nesting can reduce readability. A good comprehension should remain easy to understand and should not hide substantial business logic.",
            "Comprehensions create a new collection and can perform filtering and transformation in one expression. They are syntactic convenience rather than a fundamentally different iteration mechanism."
        ]
    },


    # ============================================================
    # MACHINE LEARNING — 10 QUESTIONS
    # ============================================================

    {
        "question": "What is supervised learning?",
        "topic": "machine_learning",
        "concepts": ["supervised-learning", "labels", "training"],
        "incorrect": [
            "Supervised learning never uses training data.",
            "It means a human manually predicts every result.",
            "Supervised learning only works for images.",
            "It is learning without any target values."
        ],
        "weak": [
            "Supervised learning learns from labeled data.",
            "The model gets examples with answers.",
            "It is used for prediction tasks.",
            "Classification is one type of supervised learning."
        ],
        "partial": [
            "Supervised learning trains a model using input examples paired with target labels or values.",
            "The model learns a mapping from features to known outcomes.",
            "Classification and regression are common supervised learning problems.",
            "The target values provide feedback during training."
        ],
        "good": [
            "Supervised learning uses labeled training data to learn a relationship between input features and target outputs. Classification and regression are common examples.",
            "During training, the model produces predictions and compares them with known targets using a loss function, allowing its parameters to be optimized.",
            "A spam classifier is a supervised learning example because training messages can be labeled as spam or not spam.",
            "The goal is usually to learn a function that generalizes from labeled training examples to unseen examples."
        ],
        "excellent": [
            "Supervised learning learns a predictive mapping from inputs to known targets. During training, predictions are compared with ground-truth labels through a loss function, and model parameters are adjusted to reduce that loss.",
            "Classification predicts discrete categories, while regression predicts continuous numerical values. Both are supervised because the training examples contain target information.",
            "The important challenge is generalization. A model that performs well on its training set but poorly on unseen data may have memorized the training examples rather than learning patterns that transfer.",
            "Supervised learning requires labeled examples for the target being learned. The quality, representativeness, and consistency of those labels strongly influence the resulting model."
        ]
    },

    {
        "question": "What is unsupervised learning?",
        "topic": "machine_learning",
        "concepts": ["unsupervised-learning", "clustering", "patterns"],
        "incorrect": [
            "Unsupervised learning requires every example to have a human-provided label.",
            "It is only used for calculating averages.",
            "It cannot discover patterns in data.",
            "Unsupervised learning is the same as supervised classification."
        ],
        "weak": [
            "Unsupervised learning works without labeled targets.",
            "It can find patterns in data.",
            "Clustering is a common example.",
            "The algorithm tries to organize the data."
        ],
        "partial": [
            "Unsupervised learning learns structure from data without explicit target labels.",
            "Clustering groups similar examples together without predefined class labels.",
            "Dimensionality reduction is another common unsupervised technique.",
            "The objective depends on the algorithm, such as grouping similar points or representing data with fewer dimensions."
        ],
        "good": [
            "Unsupervised learning analyzes data without labeled target outputs and attempts to discover useful structure, such as clusters or lower-dimensional representations.",
            "K-means clustering is a common example in which the algorithm groups observations according to similarity.",
            "Techniques such as PCA can reduce dimensionality while preserving important variation in the data.",
            "Unlike supervised learning, evaluation can be more difficult because there may not be a ground-truth target defining the correct result."
        ],
        "excellent": [
            "Unsupervised learning seeks structure in data without explicit target labels. Depending on the objective, it can perform clustering, density estimation, dimensionality reduction, or representation learning.",
            "In K-means, for example, the algorithm optimizes cluster assignments and centroids to reduce within-cluster squared distances. The resulting clusters are not automatically guaranteed to correspond to meaningful real-world categories.",
            "Unsupervised methods often require interpretation or task-specific evaluation because there is no direct target label against which predictions can simply be compared.",
            "Modern representation learning can use self-supervised objectives that technically create training targets from the data itself. This is related to unsupervised learning but is often discussed separately because the training objective is explicitly constructed."
        ]
    },

    {
        "question": "What is overfitting in machine learning?",
        "topic": "machine_learning",
        "concepts": ["overfitting", "generalization", "training"],
        "incorrect": [
            "Overfitting means the model cannot learn anything from training data.",
            "Overfitting always means the dataset is too large.",
            "An overfitted model performs equally on all datasets.",
            "Overfitting only happens in unsupervised learning."
        ],
        "weak": [
            "Overfitting happens when a model learns the training data too closely.",
            "It can cause poor performance on new data.",
            "A complex model can sometimes overfit.",
            "Regularization can help reduce overfitting."
        ],
        "partial": [
            "Overfitting occurs when a model performs well on training data but poorly on unseen data.",
            "The model may learn noise or accidental patterns instead of general relationships.",
            "More diverse training data and regularization can help improve generalization.",
            "A large gap between training and validation performance can indicate overfitting."
        ],
        "good": [
            "Overfitting occurs when a model memorizes training-specific patterns, including noise, instead of learning relationships that generalize to unseen examples.",
            "Typical signs include very low training error combined with substantially higher validation or test error.",
            "Techniques such as regularization, dropout, early stopping, data augmentation, simpler models, and more representative data can help control overfitting.",
            "Validation data should be used to detect overfitting while keeping the test set separate for final evaluation."
        ],
        "excellent": [
            "Overfitting is a generalization failure in which the model fits idiosyncrasies of the training sample too strongly. Consequently, training loss may continue decreasing while validation performance stops improving or deteriorates.",
            "It can arise from excessive model capacity, limited or repetitive data, noisy labels, data leakage, insufficient regularization, or training for too long. The appropriate remedy depends on the underlying cause.",
            "Regularization methods such as weight decay constrain parameter values, dropout changes the training computation stochastically, and early stopping limits optimization once validation performance stops improving. More representative data can be even more effective.",
            "A model should be evaluated on data that was not used to select its parameters or repeatedly tune its design. Otherwise, apparent test performance can itself become optimistic through repeated experimentation."
        ]
    },

    {
        "question": "What is underfitting in machine learning?",
        "topic": "machine_learning",
        "concepts": ["underfitting", "bias", "model-capacity"],
        "incorrect": [
            "Underfitting means the model memorizes every training example.",
            "It only occurs when a dataset contains millions of examples.",
            "Underfitting means test accuracy is always 100 percent.",
            "It is another name for data leakage."
        ],
        "weak": [
            "Underfitting means the model has not learned enough.",
            "It can happen with a model that is too simple.",
            "Both training and validation performance can be poor.",
            "A model may need more capacity to reduce underfitting."
        ],
        "partial": [
            "Underfitting occurs when a model cannot capture important patterns in the data.",
            "It often results in poor performance on both training and unseen examples.",
            "An overly simple model or excessive regularization can cause underfitting.",
            "Increasing model capacity or improving features can sometimes reduce underfitting."
        ],
        "good": [
            "Underfitting occurs when the model is too limited to represent the underlying patterns, leading to poor training performance and usually poor validation performance as well.",
            "Causes can include insufficient model capacity, excessive regularization, weak features, inadequate training, or an inappropriate model choice.",
            "A model that underfits may have both high training error and high validation error, unlike typical overfitting where training error is much lower.",
            "Possible remedies include increasing model complexity, training longer, reducing excessive regularization, or improving the input representation."
        ],
        "excellent": [
            "Underfitting is a high-bias situation where the learned function fails to capture important structure in the training distribution. Consequently, the model may perform poorly even on examples it was trained on.",
            "Underfitting can result from low-capacity models, overly strong regularization, poor features, insufficient optimization, or a mismatch between model assumptions and the data.",
            "Increasing capacity is not automatically the correct solution. One should examine training loss, validation loss, optimization behavior, feature quality, and regularization before deciding what is limiting performance.",
            "The bias-variance perspective describes underfitting as excessive bias, while overfitting is associated with excessive sensitivity to the training sample. Practical model selection attempts to find a balance that generalizes well."
        ]
    },

    {
        "question": "What is a loss function?",
        "topic": "machine_learning",
        "concepts": ["loss", "objective", "optimization"],
        "incorrect": [
            "A loss function stores the training dataset.",
            "It converts every prediction into an image.",
            "Loss is unrelated to model training.",
            "A loss function always returns a class label."
        ],
        "weak": [
            "A loss function measures model error.",
            "It tells the model how wrong its prediction is.",
            "Training tries to reduce loss.",
            "Different tasks can use different loss functions."
        ],
        "partial": [
            "A loss function maps predictions and targets to a numerical measure of error.",
            "The optimizer uses the loss and its gradients to update model parameters.",
            "Mean squared error is commonly used for regression.",
            "Cross-entropy is commonly used for classification."
        ],
        "good": [
            "A loss function quantifies the discrepancy between a model's predictions and the target values. Training generally adjusts parameters to minimize this objective.",
            "For regression, mean squared error is one common loss, while classification often uses cross-entropy.",
            "The loss provides the scalar objective whose gradients are used by optimization algorithms such as gradient descent.",
            "The training loss and the evaluation metric do not always have to be identical; a differentiable loss may be chosen because it is suitable for optimization."
        ],
        "excellent": [
            "A loss function defines how undesirable a model prediction is relative to its target. During gradient-based training, the loss is differentiated with respect to model parameters and the resulting gradients guide parameter updates.",
            "Cross-entropy measures the discrepancy between predicted probability distributions and target labels, whereas mean squared error measures squared numerical differences and is common for regression.",
            "The choice of loss encodes aspects of the learning objective. An appropriate loss should reflect the task and provide useful optimization signals; it can also affect calibration, robustness, and sensitivity to errors.",
            "The objective optimized during training may be an aggregate of multiple losses or include regularization terms. Therefore the reported training objective can contain more than the raw prediction error."
        ]
    },

    {
        "question": "What is gradient descent?",
        "topic": "machine_learning",
        "concepts": ["gradient-descent", "optimization", "learning-rate"],
        "incorrect": [
            "Gradient descent randomly changes labels.",
            "It only works for sorting numbers.",
            "Gradient descent removes the training dataset.",
            "It guarantees the global optimum for every model."
        ],
        "weak": [
            "Gradient descent is used to train models.",
            "It updates model parameters using gradients.",
            "It tries to reduce the loss.",
            "The learning rate controls the update size."
        ],
        "partial": [
            "Gradient descent changes parameters in the direction that decreases the loss.",
            "The gradient tells how the loss changes with respect to model parameters.",
            "The learning rate determines how large each update is.",
            "Training repeatedly calculates gradients and updates parameters."
        ],
        "good": [
            "Gradient descent is an optimization algorithm that iteratively updates model parameters in the negative direction of the loss gradient.",
            "The learning rate controls how far the parameters move during each update. A rate that is too high can make training unstable, while one that is too low can make training slow.",
            "In mini-batch gradient descent, gradients are estimated using a subset of training examples rather than the entire dataset.",
            "Backpropagation calculates gradients for neural networks, and an optimizer uses those gradients to update the parameters."
        ],
        "excellent": [
            "Gradient descent minimizes an objective by repeatedly applying an update of the general form parameter = parameter minus learning rate times gradient. The gradient points toward increasing loss, so moving in the negative direction tends to decrease it locally.",
            "Stochastic and mini-batch variants estimate the gradient from subsets of data, introducing noise but making optimization computationally practical for large datasets.",
            "Gradient descent does not guarantee a global optimum for arbitrary neural networks because their objectives can be non-convex. The optimization landscape can contain saddle points, flat regions, and many local structures.",
            "Modern optimizers such as Adam modify basic gradient descent by maintaining statistics of past gradients and adapting effective update sizes, often improving convergence behavior."
        ]
    },

    {
        "question": "What is a train-validation-test split?",
        "topic": "machine_learning",
        "concepts": ["dataset-split", "validation", "test"],
        "incorrect": [
            "All three sets should contain exactly the same examples.",
            "The test set should be used for every training update.",
            "The validation set replaces the training set.",
            "The split is only necessary for image datasets."
        ],
        "weak": [
            "The dataset is divided into different parts.",
            "Training data trains the model.",
            "Validation data helps choose settings.",
            "Test data measures final performance."
        ],
        "partial": [
            "Training data is used to fit model parameters.",
            "Validation data is used for model selection and hyperparameter tuning.",
            "The test set should be kept separate for an unbiased final evaluation.",
            "Keeping the test set untouched helps estimate performance on unseen data."
        ],
        "good": [
            "The training set is used to learn parameters, the validation set helps tune hyperparameters and compare models, and the test set is reserved for final evaluation.",
            "If the test set is repeatedly used to make design decisions, it can become indirectly part of the tuning process and produce an overly optimistic estimate.",
            "The exact split ratio depends on dataset size and task. With small datasets, cross-validation can sometimes provide a more efficient estimate.",
            "The split should also avoid leakage, such as placing highly related samples from the same subject in both training and test sets when the real deployment task requires subject-level generalization."
        ],
        "excellent": [
            "A train-validation-test setup separates parameter fitting, model selection, and final performance estimation. Training examples influence learned weights; validation examples influence choices such as architecture or hyperparameters; the test set should ideally remain untouched until the final evaluation.",
            "The split strategy must reflect the deployment setting. For time-dependent data, random splitting can leak future information; for grouped observations, related samples may need to remain in the same partition.",
            "When data is scarce, k-fold cross-validation can repeatedly train on different partitions and provide a more stable estimate for model selection. A final independent test set can still be retained when feasible.",
            "The purpose is not merely to create three files. It is to ensure that evaluation data represents genuinely unseen information relative to the decisions used to build the model."
        ]
    },

    {
        "question": "What is precision and recall?",
        "topic": "machine_learning",
        "concepts": ["precision", "recall", "classification"],
        "incorrect": [
            "Precision and recall are both measures of training speed.",
            "Recall measures how many features a model contains.",
            "Precision is always equal to accuracy.",
            "They are only used for regression."
        ],
        "weak": [
            "Precision and recall are classification metrics.",
            "Precision is about correct positive predictions.",
            "Recall is about finding positive examples.",
            "They are calculated using classification outcomes."
        ],
        "partial": [
            "Precision is the fraction of predicted positives that are actually positive.",
            "Recall is the fraction of actual positives that the model correctly identifies.",
            "Precision focuses on false positives while recall is strongly affected by false negatives.",
            "There is often a trade-off between precision and recall."
        ],
        "good": [
            "Precision is TP divided by TP plus FP, so it measures how reliable positive predictions are. Recall is TP divided by TP plus FN, so it measures how many actual positives were found.",
            "A system that predicts many false positives can have low precision, while a system that misses many real positives can have low recall.",
            "Precision can be especially important when false alarms are costly, while recall can matter more when missing a positive case is costly.",
            "The precision-recall trade-off can often be adjusted by changing the classification threshold."
        ],
        "excellent": [
            "Precision answers 'of the examples predicted positive, how many were truly positive?' and is TP/(TP+FP). Recall answers 'of all actual positives, how many were found?' and is TP/(TP+FN).",
            "Changing a classifier's decision threshold often moves precision and recall in opposite directions. Therefore reporting a single threshold-dependent value without understanding the application can be misleading.",
            "For imbalanced classification, precision and recall can provide more informative insight than accuracy because a high accuracy may be obtained simply by predicting the majority class.",
            "F1 combines precision and recall through their harmonic mean. It is useful when both matter, but it should not automatically replace metrics that reflect the actual costs of false positives and false negatives."
        ]
    },

    {
        "question": "What is feature scaling?",
        "topic": "machine_learning",
        "concepts": ["feature-scaling", "normalization", "standardization"],
        "incorrect": [
            "Feature scaling deletes features from a dataset.",
            "It converts classification into regression.",
            "Scaling always changes the number of examples.",
            "Feature scaling is only used for text labels."
        ],
        "weak": [
            "Feature scaling puts features on similar scales.",
            "It can help some machine learning algorithms.",
            "Normalization and standardization are examples.",
            "Large numerical ranges can affect some models."
        ],
        "partial": [
            "Feature scaling transforms numerical features so their magnitudes are comparable.",
            "Standardization commonly subtracts the mean and divides by standard deviation.",
            "Min-max scaling maps values into a selected range.",
            "Scaling is especially useful for distance-based and gradient-based algorithms."
        ],
        "good": [
            "Feature scaling prevents features with large numerical magnitudes from dominating algorithms that depend on distances or gradients.",
            "Standardization transforms a feature using its mean and standard deviation, while min-max scaling typically maps values to a fixed interval.",
            "Algorithms such as k-nearest neighbors, k-means, SVMs, and neural networks can benefit from appropriately scaled numerical features.",
            "Scaling parameters should be fitted using training data and then applied to validation and test data to avoid leakage."
        ],
        "excellent": [
            "Feature scaling changes the numerical representation of features without necessarily changing their underlying information. It can improve optimization conditioning and prevent distance-based methods from being dominated by high-magnitude variables.",
            "Standardization typically produces approximately zero-mean, unit-variance features using training-set statistics. Min-max scaling instead uses the training-set minimum and maximum to map values to a chosen interval.",
            "Tree-based models are generally much less sensitive to monotonic feature scaling because their splits depend on ordering rather than Euclidean distances or gradient magnitudes.",
            "A common leakage mistake is computing scaling statistics from the entire dataset before splitting. The transformer must be fitted only on training data, then reused unchanged on validation and test data."
        ]
    },

    {
        "question": "What is cross-validation?",
        "topic": "machine_learning",
        "concepts": ["cross-validation", "model-selection", "folds"],
        "incorrect": [
            "Cross-validation means validating only one training example.",
            "It guarantees that a model cannot overfit.",
            "Cross-validation removes the need for any data.",
            "It is a method for converting text to images."
        ],
        "weak": [
            "Cross-validation evaluates a model using multiple splits.",
            "The data is divided into folds.",
            "Different folds can be used for validation.",
            "It can provide a more stable performance estimate."
        ],
        "partial": [
            "In k-fold cross-validation, data is divided into k parts and each part is used as validation while the others are used for training.",
            "The results from the folds can be averaged to estimate performance.",
            "Cross-validation is useful for model selection when data is limited.",
            "The test set should still remain separate if an independent final evaluation is required."
        ],
        "good": [
            "K-fold cross-validation repeatedly trains a model using different subsets as validation data, allowing performance to be estimated across several partitions.",
            "Each fold serves as validation once while the remaining folds are used for training. The resulting scores can be summarized using their mean and variability.",
            "Cross-validation makes better use of limited data than a single train-validation split, although it requires training the model multiple times.",
            "For classification, stratified cross-validation can preserve approximate class proportions across folds."
        ],
        "excellent": [
            "In k-fold cross-validation, the dataset is partitioned into k folds. For each iteration, one fold is held out for validation and the remaining k-1 folds are used for fitting. The process produces multiple estimates that can be aggregated.",
            "Cross-validation is primarily a model-selection and estimation technique, not a guarantee against overfitting. If many configurations are repeatedly compared using the same folds, the selection process can itself overfit those validation results.",
            "The splitting strategy should match the data. Grouped observations may require group-aware folds, while temporal data generally requires time-respecting splits to avoid training on future information.",
            "Cross-validation increases computational cost because the model is trained multiple times. After selection, a final model is often trained using the appropriate training data and evaluated once on an untouched test set."
        ]
    },


    # ============================================================
    # DEEP LEARNING — 10 QUESTIONS
    # ============================================================

    {
        "question": "What is an artificial neural network?",
        "topic": "deep_learning",
        "concepts": ["neural-network", "neurons", "layers"],
        "incorrect": [
            "A neural network is a physical computer network.",
            "It only stores database records.",
            "Neural networks do not contain parameters.",
            "A neural network can only perform addition."
        ],
        "weak": [
            "A neural network is a machine learning model.",
            "It contains connected artificial neurons.",
            "Neural networks have layers.",
            "They learn parameters from data."
        ],
        "partial": [
            "A neural network consists of layers of parameterized units that transform input data.",
            "Neurons apply weighted operations and activation functions to produce outputs.",
            "Training adjusts weights and biases so the network performs better on its objective.",
            "Deep neural networks contain multiple layers between input and output."
        ],
        "good": [
            "An artificial neural network is a parameterized function made of interconnected layers that transform inputs into outputs. Its weights are learned during training.",
            "A typical neuron computes a weighted combination of inputs, adds a bias, and applies an activation function.",
            "Multiple layers allow a neural network to learn increasingly complex representations from data.",
            "Backpropagation and an optimizer are commonly used to train neural networks by adjusting their parameters according to the loss gradient."
        ],
        "excellent": [
            "A neural network composes parameterized transformations, usually affine operations followed by nonlinear activations. Stacking these transformations allows the network to represent complex functions.",
            "The weights and biases define the model parameters. During training, a forward pass produces predictions, a loss measures the error, backpropagation computes gradients, and an optimizer updates the parameters.",
            "Depth allows intermediate layers to construct representations useful for later layers. However, adding layers does not automatically improve generalization and can introduce optimization and regularization challenges.",
            "Modern neural networks may include specialized architectures such as convolutional networks, recurrent networks, and Transformers. The common principle is learned parameterized transformations optimized using data."
        ]
    },

    {
        "question": "What is an activation function?",
        "topic": "deep_learning",
        "concepts": ["activation", "relu", "nonlinearity"],
        "incorrect": [
            "An activation function stores model weights.",
            "It is only used to load datasets.",
            "Activation functions always return class names.",
            "An activation function replaces the optimizer."
        ],
        "weak": [
            "Activation functions are used inside neural networks.",
            "They transform neuron outputs.",
            "ReLU is a common activation function.",
            "They help neural networks learn complex patterns."
        ],
        "partial": [
            "An activation function introduces nonlinearity into a neural network.",
            "Without nonlinear activations, multiple linear layers would still represent a linear transformation.",
            "ReLU returns zero for negative inputs and the input for positive inputs.",
            "Sigmoid and tanh are other common activation functions."
        ],
        "good": [
            "Activation functions introduce nonlinear transformations between neural network layers, allowing the network to represent nonlinear relationships.",
            "ReLU is popular because it is simple and generally provides useful gradients for positive inputs.",
            "Sigmoid maps values approximately to zero through one and is often used for binary probability outputs, while softmax is commonly used for multiclass probability distributions.",
            "Choosing an activation affects optimization, gradient behavior, and the type of output the network can represent."
        ],
        "excellent": [
            "Without nonlinear activation functions, composing affine layers collapses into another affine transformation, limiting the representational power of a deep network. Activations therefore enable depth to produce richer nonlinear functions.",
            "ReLU is defined as max(0,x), while sigmoid maps a scalar to approximately (0,1). GELU provides a smoother activation and is common in Transformer architectures.",
            "Activation choice depends on location in the network and task. Hidden layers often use ReLU-family or GELU activations, while output layers use task-specific functions such as sigmoid or softmax when probabilities are required.",
            "Activations also influence gradient flow. Saturating functions can produce very small derivatives in extreme regions, while ReLU-family functions can suffer from inactive units for negative inputs, illustrating why activation selection affects optimization."
        ]
    },

    {
        "question": "What is backpropagation?",
        "topic": "deep_learning",
        "concepts": ["backpropagation", "gradients", "chain-rule"],
        "incorrect": [
            "Backpropagation sends data backward to the user.",
            "It directly creates new training examples.",
            "Backpropagation replaces the neural network.",
            "It only calculates predictions."
        ],
        "weak": [
            "Backpropagation calculates gradients.",
            "It is used to train neural networks.",
            "The error is propagated backward.",
            "The optimizer uses the calculated gradients."
        ],
        "partial": [
            "Backpropagation applies the chain rule to calculate how the loss changes with respect to network parameters.",
            "It starts from the loss and works backward through the computational graph.",
            "The calculated gradients tell the optimizer how parameters should be changed.",
            "Backpropagation itself calculates gradients; an optimizer such as Adam performs parameter updates."
        ],
        "good": [
            "Backpropagation efficiently computes gradients of the loss with respect to neural network parameters using the chain rule.",
            "After the forward pass computes predictions and loss, backpropagation propagates derivative information backward through the layers.",
            "The resulting gradients are passed to an optimization algorithm, which updates weights and biases.",
            "Automatic differentiation libraries such as PyTorch can construct a computational graph and calculate these gradients automatically."
        ],
        "excellent": [
            "Backpropagation is an application of the chain rule to a computational graph. Starting from the loss, it computes partial derivatives with respect to intermediate values and parameters in reverse order, allowing gradients to be calculated efficiently.",
            "It should be distinguished from optimization. Backpropagation determines gradients; gradient descent, Adam, or another optimizer uses those gradients to update parameters.",
            "For a network composed of many layers, naive symbolic differentiation would repeatedly recompute terms. Reverse-mode automatic differentiation makes computing gradients with respect to many parameters efficient for a scalar loss.",
            "Issues such as vanishing or exploding gradients arise when repeated derivatives through deep compositions become extremely small or large. Architecture, initialization, normalization, activations, and optimization strategies can influence these effects."
        ]
    },

    {
        "question": "What is an epoch in deep learning?",
        "topic": "deep_learning",
        "concepts": ["epoch", "training", "batches"],
        "incorrect": [
            "An epoch means one individual neuron.",
            "An epoch is the size of a model.",
            "An epoch contains only one training example.",
            "An epoch is a type of activation function."
        ],
        "weak": [
            "An epoch is one pass through the training data.",
            "Models are usually trained for multiple epochs.",
            "Each epoch contains batches.",
            "More epochs mean more training iterations."
        ],
        "partial": [
            "One epoch means the model has processed the complete training dataset once.",
            "If the dataset has 1,000 examples and the batch size is 100, one epoch involves about 10 batches.",
            "Multiple epochs allow the model to repeatedly learn from the training data.",
            "Too many epochs can contribute to overfitting."
        ],
        "good": [
            "An epoch represents one complete pass through the training dataset. With mini-batch training, the dataset is divided into batches and each batch produces an optimization update.",
            "The number of batches per epoch is approximately the number of training examples divided by batch size, subject to the data-loader configuration.",
            "Increasing epochs gives the optimizer more opportunities to adjust parameters, but validation performance should be monitored because excessive training can overfit.",
            "Epoch, batch size, and learning rate interact: changing batch size changes how many parameter updates occur during each epoch."
        ],
        "excellent": [
            "An epoch is one complete traversal of the training dataset. In mini-batch optimization, each batch usually produces a gradient computation and parameter update, so the number of updates per epoch depends on dataset size and batch size.",
            "Epochs are a convenient reporting unit rather than a fundamental optimization requirement. Training could instead be described by the total number of optimization steps or examples processed.",
            "More epochs do not necessarily improve generalization. Training loss may continue decreasing while validation performance worsens, which is why early stopping or checkpoint selection can be useful.",
            "Changing batch size changes the number of updates per epoch and can alter optimization dynamics. Therefore epoch counts should not be interpreted independently of batch size and learning-rate choices."
        ]
    },

    {
        "question": "What is dropout in neural networks?",
        "topic": "deep_learning",
        "concepts": ["dropout", "regularization", "generalization"],
        "incorrect": [
            "Dropout permanently deletes neurons from a trained model.",
            "Dropout increases every model weight.",
            "It is used only to load data.",
            "Dropout guarantees perfect generalization."
        ],
        "weak": [
            "Dropout is a regularization technique.",
            "It randomly turns off some units during training.",
            "It can reduce overfitting.",
            "Dropout behaves differently during evaluation."
        ],
        "partial": [
            "During training, dropout randomly sets some activations to zero.",
            "This can prevent the network from relying too heavily on particular units.",
            "At evaluation time, dropout is normally disabled and the full network is used.",
            "Dropout is one method for improving generalization."
        ],
        "good": [
            "Dropout randomly masks activations during training, encouraging the network to distribute information rather than relying on specific units.",
            "During evaluation, dropout is disabled and the model uses all units, with the training-time scaling handled so expected activation magnitudes remain consistent.",
            "Dropout acts as a regularizer and can reduce overfitting, although its usefulness depends on the architecture and amount of data.",
            "In PyTorch, `model.train()` enables dropout behavior while `model.eval()` disables it."
        ],
        "excellent": [
            "Dropout is stochastic regularization in which activations are randomly masked during training. With inverted dropout, surviving activations are scaled during training so that their expected magnitude remains consistent when dropout is disabled at evaluation time.",
            "The random masks encourage redundant representations and reduce reliance on individual pathways. This can improve generalization but may also slow optimization or hurt performance if used excessively.",
            "Dropout must be handled differently between training and inference. In frameworks such as PyTorch, switching between `train()` and `eval()` changes the behavior of dropout layers.",
            "Dropout is not literally deleting neurons from the model. The architecture remains present; only particular activations are temporarily suppressed during a training forward pass."
        ]
    },

    {
        "question": "What is batch normalization?",
        "topic": "deep_learning",
        "concepts": ["batch-normalization", "normalization", "training"],
        "incorrect": [
            "Batch normalization removes batches from training.",
            "It only works on labels.",
            "It permanently normalizes every dataset before training.",
            "Batch normalization is an optimizer."
        ],
        "weak": [
            "Batch normalization normalizes activations.",
            "It can make training more stable.",
            "It uses statistics from batches during training.",
            "It has learned parameters."
        ],
        "partial": [
            "Batch normalization normalizes intermediate activations using batch statistics during training.",
            "It typically has learnable scale and shift parameters.",
            "During evaluation it uses running statistics rather than the current training batch.",
            "It can help optimization and sometimes improve generalization."
        ],
        "good": [
            "Batch normalization normalizes activations using statistics computed from mini-batches during training, followed by learned scale and shift parameters.",
            "During inference, batch normalization normally uses running estimates accumulated during training rather than statistics from the current batch.",
            "It can make optimization more stable and sometimes allow larger learning rates.",
            "The behavior difference between training and evaluation means correct mode switching is important when using batch normalization."
        ],
        "excellent": [
            "Batch normalization transforms activations using batch mean and variance, then applies learned scale and shift parameters. Training uses current mini-batch statistics while inference generally uses running estimates.",
            "Because the statistics depend on the batch, batch size and distribution can influence its behavior. This is one reason alternative normalization methods such as layer normalization are common in sequence models and Transformers.",
            "Batch normalization changes the optimization landscape and can provide regularizing effects, but its original interpretation as simply 'fixing internal covariate shift' is an incomplete description of why it can help.",
            "When evaluating a model containing batch normalization, using evaluation mode is important because the layer should use its stored running statistics instead of continuously updating statistics from evaluation batches."
        ]
    },

    {
        "question": "What is a convolutional neural network?",
        "topic": "deep_learning",
        "concepts": ["cnn", "convolution", "images"],
        "incorrect": [
            "A CNN is a database management system.",
            "CNNs cannot process images.",
            "A convolution means randomly deleting pixels.",
            "CNNs contain no trainable parameters."
        ],
        "weak": [
            "CNNs are commonly used for images.",
            "They use convolutional layers.",
            "CNNs can learn visual features.",
            "Filters are used to process local regions."
        ],
        "partial": [
            "A convolutional neural network uses learned filters to process local regions of an input.",
            "Convolutional layers can learn features such as edges and more complex patterns.",
            "CNNs exploit local spatial structure and shared weights.",
            "Pooling or striding can reduce spatial dimensions."
        ],
        "good": [
            "CNNs use convolutional operations with shared filters to extract local spatial features. They are particularly effective for images because nearby pixels often have meaningful relationships.",
            "Early convolutional layers can learn simple patterns while deeper layers combine them into more complex representations.",
            "Weight sharing means the same filter parameters are applied across different spatial positions, reducing the number of parameters compared with fully connected layers.",
            "Strides and pooling can reduce spatial resolution and increase the receptive field of later layers."
        ],
        "excellent": [
            "A convolutional neural network exploits spatial locality and translation-related structure through kernels whose weights are shared across positions. This gives convolutional layers strong inductive biases for grid-like data such as images.",
            "A convolutional layer produces feature maps by applying learned kernels, with choices such as stride, padding, and kernel size controlling spatial dimensions and receptive fields.",
            "Deeper CNN layers can combine lower-level features into increasingly abstract representations. Pooling or strided convolutions can reduce resolution while allowing later features to incorporate broader context.",
            "Although CNNs are strongly associated with computer vision, convolutional architectures can also process other structured signals such as audio spectrograms, time series, and sequences when local patterns are useful."
        ]
    },

    {
        "question": "What is an RNN?",
        "topic": "deep_learning",
        "concepts": ["rnn", "sequence", "hidden-state"],
        "incorrect": [
            "An RNN can only process unordered tables.",
            "RNNs have no hidden state.",
            "An RNN is a type of database.",
            "RNNs process all sequences without considering order."
        ],
        "weak": [
            "RNN stands for recurrent neural network.",
            "It is used for sequential data.",
            "RNNs maintain information from previous steps.",
            "They can process text sequences."
        ],
        "partial": [
            "An RNN processes a sequence one step at a time while maintaining a hidden state.",
            "The hidden state carries information from previous sequence positions.",
            "RNNs can be used for language, time series, and other sequential data.",
            "Basic RNNs can have difficulty learning long-range dependencies."
        ],
        "good": [
            "A recurrent neural network processes sequential inputs while maintaining a hidden state that summarizes information from earlier time steps.",
            "At each step, the current input and previous hidden state are combined to produce a new hidden state and possibly an output.",
            "RNNs are naturally suited to variable-length sequences, but standard RNNs can suffer from vanishing or exploding gradients when learning long dependencies.",
            "LSTM and GRU architectures were designed to improve the ability of recurrent networks to retain useful information over longer sequences."
        ],
        "excellent": [
            "An RNN applies a recurrent transition across sequence positions, carrying a hidden state from one time step to the next. This creates parameter sharing across positions and allows sequential information to influence later outputs.",
            "During training, gradients are propagated through the unrolled sequence, which can produce vanishing or exploding gradients for long sequences. Gated architectures such as LSTMs and GRUs introduce mechanisms that improve information flow.",
            "RNNs process tokens sequentially, which limits parallelism compared with Transformers. Transformers instead use attention to relate positions more directly and can process many positions in parallel during training.",
            "RNNs remain useful in some streaming and resource-constrained applications, but their sequential computation and difficulty with long-range dependencies contributed to the widespread adoption of attention-based architectures."
        ]
    },

    {
        "question": "What is an embedding in deep learning?",
        "topic": "deep_learning",
        "concepts": ["embedding", "representation", "vectors"],
        "incorrect": [
            "An embedding is a database table with no numerical values.",
            "Embeddings are always images.",
            "An embedding removes semantic information.",
            "Embeddings can only contain one dimension."
        ],
        "weak": [
            "An embedding represents something as a vector.",
            "Words can be converted into embeddings.",
            "Similar things can have similar vectors.",
            "Embeddings are learned representations."
        ],
        "partial": [
            "An embedding maps discrete items such as words or tokens into continuous numerical vectors.",
            "The model can learn vector representations where useful relationships are encoded geometrically.",
            "Token embeddings are commonly used as inputs to neural language models.",
            "Embedding dimensions are learned parameters during training unless a fixed pretrained embedding is used."
        ],
        "good": [
            "An embedding is a dense vector representation of an item such as a token, user, document, or category. Neural networks can learn embeddings that capture useful relationships for a task.",
            "In language models, token IDs are mapped through an embedding matrix to dense vectors before further neural processing.",
            "Embedding vectors can be compared using measures such as cosine similarity, depending on how they were trained and what task they represent.",
            "Embeddings are useful because continuous vector spaces allow machine learning models to operate on categorical or symbolic information numerically."
        ],
        "excellent": [
            "An embedding is a learned or fixed vector representation that maps discrete or structured objects into a continuous numerical space. In a neural network, a token embedding table can be viewed as a matrix indexed by token IDs.",
            "Semantic similarity is not guaranteed merely because vectors are called embeddings; the geometry depends on the training objective and data. Embeddings trained for different tasks can encode very different notions of similarity.",
            "Sentence and document embeddings are often produced by encoder models and can be indexed for semantic retrieval. Their usefulness for retrieval depends on the embedding model, pooling method, normalization, and domain.",
            "Embedding layers are differentiable lookup operations. During training, the vectors corresponding to observed IDs receive gradient updates, allowing representations to specialize to the learning objective."
        ]
    },

    {
        "question": "What is transfer learning?",
        "topic": "deep_learning",
        "concepts": ["transfer-learning", "pretraining", "fine-tuning"],
        "incorrect": [
            "Transfer learning means copying a dataset to another computer.",
            "It requires training every model from scratch.",
            "Transfer learning cannot use pretrained models.",
            "It only applies to databases."
        ],
        "weak": [
            "Transfer learning reuses knowledge from another model.",
            "A pretrained model can be adapted to another task.",
            "It can reduce training requirements.",
            "Fine-tuning is related to transfer learning."
        ],
        "partial": [
            "Transfer learning starts with representations learned from one task or dataset and adapts them to another task.",
            "A pretrained model can be fine-tuned using a smaller task-specific dataset.",
            "Some layers can be frozen while other layers are trained.",
            "Transfer learning is useful when the target dataset is smaller than the data used for pretraining."
        ],
        "good": [
            "Transfer learning reuses a model or representation learned from a source task and adapts it to a target task. Fine-tuning is a common approach.",
            "A pretrained vision model, for example, can be adapted to a new image classification problem rather than learning all visual features from scratch.",
            "Freezing early layers can reduce the number of trainable parameters, while fine-tuning more layers allows the representation to adapt to the new domain.",
            "The benefit depends on how related the source and target domains are and how much target data is available."
        ],
        "excellent": [
            "Transfer learning leverages information learned from a source distribution or task to improve learning on a target task. In deep learning, pretrained representations often provide useful features that can be adapted with substantially less target data.",
            "Fine-tuning updates some or all pretrained parameters on the target objective. Alternatives include freezing the backbone and training a new head, or using parameter-efficient methods such as adapters or low-rank updates.",
            "Transfer can fail or provide limited benefit when the source and target distributions differ substantially. Negative transfer is possible when inherited representations bias the model toward patterns that are unhelpful for the target task.",
            "Large language models and modern vision models rely heavily on transfer learning: broad pretraining creates general representations, followed by adaptation for specific tasks, domains, or instruction-following behavior."
        ]
    },


    # ============================================================
    # TRANSFORMERS — 10 QUESTIONS
    # ============================================================

    {
        "question": "What is a Transformer?",
        "topic": "transformers",
        "concepts": ["transformer", "attention", "sequence"],
        "incorrect": [
            "A Transformer is only an electrical device in machine learning.",
            "Transformers cannot process text.",
            "A Transformer is a database engine.",
            "Transformers do not contain learned parameters."
        ],
        "weak": [
            "A Transformer is a neural network architecture.",
            "It is widely used for language tasks.",
            "Transformers use attention.",
            "They can process sequences."
        ],
        "partial": [
            "A Transformer is a neural architecture based heavily on attention mechanisms.",
            "It can model relationships between different positions in a sequence.",
            "Transformers commonly contain attention and feed-forward layers.",
            "They are widely used in language models and other sequence tasks."
        ],
        "good": [
            "A Transformer is a neural network architecture that uses self-attention to model relationships between sequence positions. It also uses feed-forward layers, normalization, residual connections, and positional information.",
            "Transformers became popular because attention allows tokens to interact directly and training can be highly parallelized compared with recurrent architectures.",
            "Encoder-only, decoder-only, and encoder-decoder Transformer architectures are used for different tasks.",
            "Modern large language models commonly use decoder-style Transformers to predict the next token given previous context."
        ],
        "excellent": [
            "A Transformer is an attention-based neural architecture introduced for sequence modeling. Its core blocks combine multi-head attention with position-wise feed-forward transformations, residual connections, normalization, and positional information.",
            "Self-attention allows each position to compute weighted interactions with other positions in the context. Unlike a standard RNN, the architecture does not require processing tokens sequentially during training, which enables substantial parallelism.",
            "Encoder-only models are often used for representation or classification tasks, decoder-only models are common for autoregressive generation, and encoder-decoder models are suited to sequence-to-sequence tasks such as translation.",
            "The basic Transformer architecture has evolved into many variants, including models with different positional encoding methods, attention optimizations, normalization schemes, and parameter-efficient adaptation techniques."
        ]
    },

    {
        "question": "What is self-attention?",
        "topic": "transformers",
        "concepts": ["self-attention", "query", "key", "value"],
        "incorrect": [
            "Self-attention means a model talks to itself using audio.",
            "It compares only the first token with itself.",
            "Self-attention does not use vectors.",
            "It removes relationships between tokens."
        ],
        "weak": [
            "Self-attention lets tokens pay attention to other tokens.",
            "It helps understand context.",
            "It uses queries, keys, and values.",
            "Attention weights determine how information is combined."
        ],
        "partial": [
            "Self-attention creates queries, keys, and values from the input representations.",
            "Query-key similarities determine attention scores.",
            "The scores are normalized and used to combine value vectors.",
            "This allows each token representation to incorporate information from other positions."
        ],
        "good": [
            "Self-attention computes interactions between sequence positions by comparing query vectors with key vectors and using the resulting weights to combine value vectors.",
            "The standard scaled dot-product attention is approximately softmax(QK-transpose divided by the square root of the key dimension) multiplied by V.",
            "This mechanism lets a token dynamically gather information from relevant positions in the context.",
            "Self-attention can be masked in decoder models so a token cannot attend to future tokens during autoregressive training."
        ],
        "excellent": [
            "In scaled dot-product self-attention, each input representation is projected into queries, keys, and values. Attention weights are computed from query-key dot products, scaled by the square root of key dimension, normalized with softmax, and used to form weighted sums of values.",
            "Because Q, K, and V are derived from the same sequence, the mechanism is called self-attention. Each position can therefore construct a context-dependent representation based on other positions.",
            "Decoder-only language models use causal masking to prevent information from future tokens from influencing the representation used to predict the current next token. This preserves the autoregressive objective.",
            "Attention provides flexible content-based interactions, but standard self-attention has quadratic computational and memory complexity with respect to sequence length, motivating efficient attention variants for long contexts."
        ]
    },

    {
        "question": "What are query, key, and value in attention?",
        "topic": "transformers",
        "concepts": ["query", "key", "value", "attention"],
        "incorrect": [
            "Queries are questions asked by the user and keys are passwords.",
            "Values are always numerical labels.",
            "Keys determine the final output without using values.",
            "Queries, keys, and values are unrelated to attention."
        ],
        "weak": [
            "Queries search for relevant information.",
            "Keys are compared with queries.",
            "Values contain information to combine.",
            "Together they implement attention."
        ],
        "partial": [
            "A query represents what a position is looking for, while keys represent what each position offers for matching.",
            "The similarity between a query and key produces an attention score.",
            "The resulting weights are applied to value vectors to produce the attention output.",
            "Q, K, and V are usually learned projections of the input representations."
        ],
        "good": [
            "Queries are used to determine what information a position needs, keys determine how relevant each candidate position is, and values provide the information that gets aggregated.",
            "Attention first compares each query with keys, converts those similarities into weights, and then computes a weighted combination of values.",
            "In self-attention, Q, K, and V come from the same sequence, while in cross-attention they can come from different sequences.",
            "The separation between matching information in keys and content information in values makes attention more flexible."
        ],
        "excellent": [
            "Queries, keys, and values are learned projections of representations. A query interacts with keys to calculate compatibility scores, while the corresponding values are weighted according to those scores to produce the output representation.",
            "In self-attention, all three projections originate from the same sequence, whereas cross-attention commonly uses queries from one representation and keys and values from another.",
            "The analogy is similar to information retrieval: a query describes what is being sought, keys determine which entries are relevant, and values contain the information returned after weighting.",
            "Multi-head attention uses separate learned projections for multiple Q-K-V subspaces, allowing different heads to model different relationships before their outputs are combined."
        ]
    },

    {
        "question": "Why do Transformers need positional information?",
        "topic": "transformers",
        "concepts": ["position", "positional-encoding", "sequence-order"],
        "incorrect": [
            "Positional information is only used to reduce model size.",
            "Transformers automatically know word order without any position signal.",
            "Position information converts text into images.",
            "It is used only after the final prediction."
        ],
        "weak": [
            "Attention by itself does not directly represent sequence order.",
            "Positional information tells the model where tokens occur.",
            "It helps distinguish different arrangements of tokens.",
            "Positional encodings are one way to provide this information."
        ],
        "partial": [
            "Self-attention can treat inputs similarly regardless of their order unless position information is included.",
            "Positional encodings or learned position embeddings add information about token positions.",
            "Position allows the model to distinguish sequences with the same tokens in different orders.",
            "Different Transformer architectures use different positional representation methods."
        ],
        "good": [
            "Self-attention is largely permutation-equivariant, so a Transformer needs some mechanism to represent token order. Positional encodings or learned positional embeddings provide this information.",
            "Absolute position methods assign representations to positions, while relative or rotary approaches encode relationships between positions in other ways.",
            "Without positional information, sequences containing the same tokens in different orders would be difficult to distinguish based purely on content attention.",
            "Modern language models may use techniques such as rotary positional embeddings rather than simply adding a fixed positional vector to every token."
        ],
        "excellent": [
            "Attention alone does not inherently encode sequence order. If the same set of token representations is permuted, the attention mechanism can produce correspondingly permuted outputs. Positional information breaks this symmetry.",
            "Positional representations can be absolute, relative, learned, fixed, or incorporated directly into attention computations. Different choices affect extrapolation, efficiency, and how positional relationships are represented.",
            "Rotary positional embeddings, for example, modify query and key representations so their interactions encode relative positional relationships. This differs conceptually from simply adding a position vector to token embeddings.",
            "Position handling becomes especially important for long-context models because the chosen positional mechanism influences how well the model can represent or generalize to sequence lengths beyond those seen during training."
        ]
    },

    {
        "question": "What is multi-head attention?",
        "topic": "transformers",
        "concepts": ["multi-head", "attention", "representation"],
        "incorrect": [
            "Multi-head attention means using multiple CPUs.",
            "Each head must predict a different class.",
            "Multi-head attention removes the value vectors.",
            "It is only useful for image resizing."
        ],
        "weak": [
            "Multi-head attention uses several attention heads.",
            "Each head can learn different relationships.",
            "The outputs of the heads are combined.",
            "It is part of the Transformer architecture."
        ],
        "partial": [
            "Multi-head attention performs attention in multiple learned representation subspaces.",
            "Each head has its own query, key, and value projections.",
            "The head outputs are concatenated and projected to produce the final result.",
            "Different heads can focus on different relationships between tokens."
        ],
        "good": [
            "Multi-head attention runs several attention mechanisms in parallel using different learned projections of Q, K, and V.",
            "Each head can learn to focus on different types of relationships, such as local context, syntactic patterns, or long-range dependencies.",
            "The outputs of all heads are concatenated and passed through a learned output projection.",
            "Using multiple heads gives the model several attention subspaces rather than forcing all relationships into one attention calculation."
        ],
        "excellent": [
            "Multi-head attention splits the model representation into multiple learned subspaces. Each head independently computes scaled dot-product attention, and the resulting representations are concatenated and transformed through an output projection.",
            "Different heads can specialize in different interaction patterns, although the exact interpretability of individual heads should not be assumed without analysis.",
            "If the model dimension is d and there are h heads, each head commonly operates on a smaller dimension such as d/h, allowing multiple attention patterns without multiplying the overall representation dimension by h.",
            "Multi-head attention increases representational flexibility because the model can simultaneously compute different query-key relationships and combine the resulting context-dependent representations."
        ]
    },

    {
        "question": "What is a Transformer encoder?",
        "topic": "transformers",
        "concepts": ["encoder", "transformer", "bidirectional"],
        "incorrect": [
            "An encoder only converts Python code to machine code.",
            "An encoder cannot use attention.",
            "An encoder is always responsible for text generation.",
            "Encoder layers contain no representations."
        ],
        "weak": [
            "An encoder processes an input sequence.",
            "It uses self-attention.",
            "Encoder outputs contain contextual information.",
            "Encoders are used in models such as BERT."
        ],
        "partial": [
            "A Transformer encoder processes the input sequence using self-attention and feed-forward layers.",
            "Encoder representations can incorporate information from multiple positions in the input.",
            "Encoder-only models are useful for classification and representation tasks.",
            "BERT is a well-known encoder-based Transformer model."
        ],
        "good": [
            "A Transformer encoder converts an input sequence into contextual representations using self-attention, feed-forward networks, residual connections, and normalization.",
            "In a standard encoder, tokens can attend to other relevant tokens across the input rather than being restricted to previous positions.",
            "Encoder-based models are often useful for classification, semantic representation, retrieval, and token-level prediction.",
            "BERT uses Transformer encoder layers and was pretrained using objectives designed to learn bidirectional contextual representations."
        ],
        "excellent": [
            "A Transformer encoder is a stack of blocks that repeatedly applies self-attention and position-wise feed-forward transformations to create contextual representations. In the standard bidirectional setting, a token can incorporate information from both earlier and later positions.",
            "Encoder representations are useful when the entire input is available and the task requires understanding rather than left-to-right generation. Examples include classification, semantic similarity, and retrieval.",
            "BERT's encoder architecture uses bidirectional self-attention, meaning its representations can depend on tokens on both sides of a position. This differs from causal decoder-only language models.",
            "An encoder does not inherently mean 'non-generative.' The architectural distinction concerns how information flows and what objective the model is trained for; an encoder representation can be used as part of larger systems."
        ]
    },

    {
        "question": "What is a Transformer decoder?",
        "topic": "transformers",
        "concepts": ["decoder", "causal-attention", "generation"],
        "incorrect": [
            "A decoder can only read the last token.",
            "A decoder never uses attention.",
            "Decoder models cannot generate text.",
            "A decoder is identical to a database decoder."
        ],
        "weak": [
            "A decoder is used for generating sequences.",
            "It can use causal attention.",
            "GPT-style models use decoder architectures.",
            "The decoder predicts tokens."
        ],
        "partial": [
            "A decoder-only Transformer predicts tokens using previous context.",
            "Causal masking prevents a position from attending to future tokens.",
            "Decoder blocks commonly contain masked self-attention and feed-forward layers.",
            "In encoder-decoder models, a decoder can also use cross-attention to encoder outputs."
        ],
        "good": [
            "A decoder-only Transformer uses causal self-attention so each token can attend only to permitted previous context. This makes it suitable for autoregressive next-token prediction.",
            "GPT-style language models are commonly based on decoder-only Transformers.",
            "In an encoder-decoder Transformer, the decoder can use both masked self-attention and cross-attention to representations produced by the encoder.",
            "During generation, the decoder repeatedly predicts the next token and feeds that token back into the context."
        ],
        "excellent": [
            "A Transformer decoder used for autoregressive language modeling applies causal self-attention so predictions at position t cannot depend on future tokens. The model is trained to estimate the probability of the next token conditioned on preceding context.",
            "Decoder-only architectures such as GPT-style models differ from encoder-only models mainly in information-flow constraints and training objectives. The decoder's causal mask enforces the left-to-right generation structure.",
            "The original encoder-decoder Transformer decoder contains masked self-attention followed by cross-attention to encoder outputs. This allows generation to depend on both previously generated tokens and the encoded source sequence.",
            "Autoregressive generation repeatedly selects or samples a next token, appends it to the context, and performs another forward step. KV caching can avoid recomputing attention projections for all previous tokens during inference."
        ]
    },

    {
        "question": "What is the difference between encoder and decoder in a Transformer?",
        "topic": "transformers",
        "concepts": ["encoder", "decoder", "transformer"],
        "incorrect": [
            "The encoder and decoder are identical and always perform the same task.",
            "The encoder only handles numbers and the decoder only handles strings.",
            "The decoder never uses attention.",
            "The encoder is responsible for database storage."
        ],
        "weak": [
            "The encoder processes input while the decoder generates output.",
            "Encoders understand representations and decoders can generate sequences.",
            "They use attention differently.",
            "Some models use only one of them."
        ],
        "partial": [
            "An encoder produces contextual representations of an input, while a decoder is designed for autoregressive generation or output sequence production.",
            "Encoder-only models often support understanding tasks, while decoder-only models are common for text generation.",
            "The original Transformer decoder also uses cross-attention to encoder outputs.",
            "Decoder self-attention is typically masked for autoregressive generation."
        ],
        "good": [
            "An encoder transforms an input into contextual representations, while a decoder produces output tokens using previous output context and, in encoder-decoder models, information from the encoder.",
            "BERT is encoder-only and GPT-style models are decoder-only. T5-style sequence-to-sequence models use both encoder and decoder components.",
            "Encoder self-attention can usually access the complete input, whereas decoder self-attention is causally masked when used for autoregressive generation.",
            "Cross-attention in an encoder-decoder architecture allows decoder queries to attend to encoder-generated keys and values."
        ],
        "excellent": [
            "The encoder and decoder differ primarily in information flow and role. An encoder builds contextual representations from an input sequence, while an autoregressive decoder generates outputs subject to a causal constraint. In an encoder-decoder architecture, the decoder also cross-attends to encoder representations.",
            "Encoder-only models such as BERT are optimized for representation and understanding tasks, decoder-only models such as GPT-style systems are optimized for causal generation, and encoder-decoder models such as T5 are designed for conditional sequence generation.",
            "The decoder's causal mask prevents future target tokens from influencing earlier predictions. Cross-attention, when present, provides a separate channel through which decoder positions access encoded source information.",
            "These categories are architectural conventions rather than rigid task boundaries. What a Transformer can do depends on its architecture, attention masks, training objective, data, and downstream adaptation."
        ]
    },

    {
        "question": "What is a Transformer feed-forward network?",
        "topic": "transformers",
        "concepts": ["feed-forward", "mlp", "transformer"],
        "incorrect": [
            "It sends data directly to the internet.",
            "It replaces self-attention completely.",
            "It stores the training labels.",
            "It only performs tokenization."
        ],
        "weak": [
            "It is a neural network inside a Transformer block.",
            "It processes token representations.",
            "It usually contains linear layers and an activation.",
            "It is applied after attention in many Transformer designs."
        ],
        "partial": [
            "The Transformer feed-forward network is typically an MLP applied independently to each token position.",
            "It commonly expands the representation dimension and then projects it back.",
            "An activation such as GELU is often used between the linear layers.",
            "The feed-forward network provides nonlinear transformation after attention."
        ],
        "good": [
            "A Transformer feed-forward network, often called an MLP, applies the same small neural network independently to each sequence position.",
            "A common design expands the hidden dimension, applies a nonlinear activation, and projects the result back to the model dimension.",
            "Attention mixes information across positions, while the feed-forward network performs position-wise nonlinear processing of each resulting representation.",
            "Modern architectures may use variants such as gated MLPs rather than a simple two-layer feed-forward network."
        ],
        "excellent": [
            "The position-wise feed-forward network provides nonlinear transformation within each Transformer block. A conventional form is Linear → activation → Linear, with the same parameters applied independently at every sequence position.",
            "Attention is responsible for content-dependent communication between positions, whereas the feed-forward sublayer transforms each position's representation after that communication has occurred.",
            "The intermediate dimension is typically larger than the model dimension, giving the MLP substantial parameter capacity. Gated variants such as SwiGLU modify this structure and are common in modern language models.",
            "Residual connections allow the transformed representation to be combined with the block input, while normalization and activation choices influence optimization and representation quality."
        ]
    },

    {
        "question": "What is causal masking in Transformers?",
        "topic": "transformers",
        "concepts": ["causal-mask", "autoregressive", "attention"],
        "incorrect": [
            "Causal masking removes all previous tokens.",
            "It allows a token to see every future token.",
            "Causal masking is only for image compression.",
            "It changes labels into embeddings."
        ],
        "weak": [
            "Causal masking hides future tokens.",
            "It is used in autoregressive language models.",
            "It prevents information leakage from the future.",
            "GPT-style models use causal masking."
        ],
        "partial": [
            "Causal masking prevents position i from attending to positions after i.",
            "This allows a model to predict the next token without seeing the answer token in advance.",
            "The attention matrix is typically masked in an upper-triangular pattern.",
            "Causal masking makes self-attention compatible with left-to-right generation."
        ],
        "good": [
            "Causal masking restricts self-attention so each position can attend only to itself and earlier positions. This prevents future information from leaking into autoregressive predictions.",
            "During language-model training, the model can process the sequence in parallel while the mask ensures that each next-token prediction uses only permitted context.",
            "Without causal masking, a decoder trained for next-token prediction could directly access future tokens and the learning objective would be invalid.",
            "At generation time the model naturally has only previously generated tokens, but the same causal structure is enforced during training through the mask."
        ],
        "excellent": [
            "Causal masking sets attention scores for future positions to an effectively inaccessible value before softmax, preventing position i from using information from positions greater than i.",
            "This creates an autoregressive factorization of the sequence probability: each token is predicted conditioned only on preceding tokens. Importantly, training can still compute all positions in parallel because the mask enforces the required dependency pattern.",
            "Causal masking is different from padding masks. A causal mask represents temporal information flow, while a padding mask prevents attention to artificial padding positions.",
            "During inference, causal generation is naturally sequential because future tokens do not yet exist. KV caching improves efficiency by reusing previously computed key and value states."
        ]
    },


    # ============================================================
    # GENERATIVE AI / LLM — 10 QUESTIONS
    # ============================================================

    {
        "question": "What is a large language model?",
        "topic": "generative_ai",
        "concepts": ["llm", "language-model", "generation"],
        "incorrect": [
            "An LLM is a database containing every possible answer.",
            "An LLM only performs arithmetic calculations.",
            "LLMs do not use neural networks.",
            "An LLM is simply a search engine."
        ],
        "weak": [
            "An LLM is a large AI model trained on text.",
            "It can generate and understand language.",
            "LLMs are commonly based on Transformers.",
            "They predict tokens."
        ],
        "partial": [
            "A large language model is a neural model trained on large amounts of text to model language patterns.",
            "Many modern LLMs use Transformer architectures and learn to predict tokens.",
            "After pretraining, an LLM can be adapted for tasks such as question answering, summarization, and coding.",
            "An LLM generates text by repeatedly predicting likely next tokens."
        ],
        "good": [
            "An LLM is a neural language model with a large number of learned parameters, commonly pretrained on large text corpora. Modern LLMs are often based on Transformer architectures.",
            "During autoregressive pretraining, the model learns to predict the next token given previous context. This objective allows it to learn many linguistic and world-pattern representations.",
            "LLMs can perform generation, summarization, classification, reasoning-style tasks, and code generation depending on training and prompting.",
            "The model does not retrieve a database entry for every answer; it generates output based on learned parameters and the context provided at inference time."
        ],
        "excellent": [
            "A large language model is a parameterized neural network trained to model sequences of tokens. Many current LLMs use decoder-only Transformers and autoregressive next-token prediction during large-scale pretraining.",
            "The model's parameters encode statistical and representational patterns learned from training data. At inference, the model conditions on a context and produces a probability distribution over possible next tokens, from which generation can proceed.",
            "Instruction tuning, preference optimization, tool use, and retrieval can substantially change how a pretrained language model behaves without changing the basic concept of token-level language modeling.",
            "An LLM should not be treated as a guaranteed factual database. It can produce plausible but incorrect statements, making grounding, retrieval, validation, and appropriate evaluation important for production systems."
        ]
    },

    {
        "question": "What is tokenization in NLP?",
        "topic": "generative_ai",
        "concepts": ["tokenization", "tokens", "nlp"],
        "incorrect": [
            "Tokenization converts text directly into images.",
            "A token is always exactly one English word.",
            "Tokenization is the same as model training.",
            "Tokenization removes every punctuation mark by definition."
        ],
        "weak": [
            "Tokenization breaks text into smaller units.",
            "The units are called tokens.",
            "Models process tokens rather than raw text.",
            "Tokens can be words or word pieces."
        ],
        "partial": [
            "Tokenization converts text into a sequence of tokens that a language model can process.",
            "Tokens may represent whole words, subwords, punctuation, or other pieces depending on the tokenizer.",
            "Each token is mapped to an integer ID before entering the model.",
            "The tokenizer vocabulary determines how text is segmented."
        ],
        "good": [
            "Tokenization maps raw text into discrete tokens according to a tokenizer vocabulary. Each token is then represented by an integer ID that the model can process.",
            "Modern LLM tokenizers often use subword units so they can represent common words efficiently while still handling uncommon words by combining smaller pieces.",
            "Token count matters because model context windows and inference costs are generally measured in tokens rather than characters or words.",
            "Different tokenizers can produce different token sequences and therefore different token counts for the same text."
        ],
        "excellent": [
            "Tokenization is the deterministic preprocessing step that maps text into a sequence of vocabulary items. The resulting token IDs index embedding vectors used by the neural model.",
            "Subword tokenization provides a compromise between word-level and character-level representations: common sequences can receive individual tokens while unfamiliar strings can be decomposed into smaller units.",
            "Tokenization is model-specific. A prompt's token count, cost, and context usage therefore depend on the tokenizer associated with the model rather than simply the number of words in the prompt.",
            "Special tokens can encode structural information such as sequence boundaries, roles, or padding. Their treatment must match the model's expected tokenizer and input format."
        ]
    },

    {
        "question": "What is prompt engineering?",
        "topic": "generative_ai",
        "concepts": ["prompt-engineering", "instructions", "llm"],
        "incorrect": [
            "Prompt engineering means changing the model's neural weights manually.",
            "It requires retraining the entire LLM for every question.",
            "A prompt is only useful for image files.",
            "Prompt engineering guarantees factual answers."
        ],
        "weak": [
            "Prompt engineering means writing better prompts.",
            "It gives the model instructions.",
            "Examples can be included in prompts.",
            "Clear instructions can improve outputs."
        ],
        "partial": [
            "Prompt engineering designs instructions and context to guide an LLM toward a desired output.",
            "A prompt can specify the task, constraints, format, and relevant information.",
            "Few-shot prompting provides examples to demonstrate the expected behavior.",
            "Good prompts can reduce ambiguity and improve consistency."
        ],
        "good": [
            "Prompt engineering is the practice of designing instructions, context, examples, and output requirements so that a language model performs a task more reliably.",
            "A well-designed prompt can define the model's role, provide relevant context, specify constraints, and require a structured output format.",
            "Few-shot prompting demonstrates the desired input-output pattern using examples, while zero-shot prompting gives instructions without examples.",
            "Prompt engineering can improve behavior without modifying the model's parameters, although it cannot eliminate fundamental model limitations."
        ],
        "excellent": [
            "Prompt engineering treats the model's input context as an interface for specifying a task. Effective prompts reduce ambiguity by clearly defining goals, constraints, context, examples, and output schemas.",
            "Few-shot examples can establish task format and decision boundaries, but examples also consume context and can introduce biases. Prompt design therefore involves balancing guidance against available context.",
            "Structured output requirements such as JSON schemas can make downstream integration more reliable, but validation should still occur because a language model can produce malformed or semantically incorrect content.",
            "Prompt engineering is not equivalent to model training. It changes the inference-time context, whereas fine-tuning changes model parameters or adapter parameters using additional training data."
        ]
    },

    {
        "question": "What is temperature in text generation?",
        "topic": "generative_ai",
        "concepts": ["temperature", "sampling", "generation"],
        "incorrect": [
            "Temperature changes the physical temperature of the computer.",
            "Temperature determines the model's number of parameters.",
            "A higher temperature always makes answers more accurate.",
            "Temperature controls GPU temperature."
        ],
        "weak": [
            "Temperature controls randomness during generation.",
            "Higher temperature can produce more varied output.",
            "Lower temperature is more deterministic.",
            "It is used with token probabilities."
        ],
        "partial": [
            "Temperature modifies the sharpness of the probability distribution used during token sampling.",
            "Lower temperature makes high-probability tokens more dominant.",
            "Higher temperature makes lower-probability alternatives relatively more likely.",
            "Temperature affects diversity rather than directly changing the model's learned knowledge."
        ],
        "good": [
            "Temperature rescales logits before sampling. Lower values make the distribution more concentrated around high-probability tokens, while higher values produce a flatter distribution and potentially more diverse outputs.",
            "A temperature near zero generally makes generation more deterministic, although exact behavior depends on the API and decoding implementation.",
            "Higher temperature can increase creativity but also increase the chance of incoherent or incorrect outputs.",
            "Temperature is a decoding parameter; changing it does not retrain or modify the model's weights."
        ],
        "excellent": [
            "Temperature modifies token logits before softmax, conceptually producing probabilities proportional to exp(logit divided by temperature). Lower temperature sharpens the distribution, while higher temperature flattens it.",
            "Temperature primarily changes sampling behavior rather than the underlying model. It therefore cannot add factual knowledge that the model did not learn or retrieve from context.",
            "Very low temperatures can make outputs repetitive or overly deterministic, while high temperatures can increase diversity and variance. The appropriate value depends on whether consistency or exploration is more important.",
            "Temperature interacts with other decoding controls such as top-k and top-p sampling. Therefore observed generation behavior cannot always be attributed to temperature alone."
        ]
    },

    {
        "question": "What is fine-tuning of an LLM?",
        "topic": "generative_ai",
        "concepts": ["fine-tuning", "training", "llm"],
        "incorrect": [
            "Fine-tuning means changing the font size of an LLM.",
            "Fine-tuning never uses training examples.",
            "It is the same as writing a prompt.",
            "Fine-tuning removes all pretrained knowledge."
        ],
        "weak": [
            "Fine-tuning trains a pretrained model further.",
            "It uses task-specific data.",
            "It can adapt model behavior.",
            "Fine-tuning changes model parameters."
        ],
        "partial": [
            "Fine-tuning continues training a pretrained model on a task- or domain-specific dataset.",
            "It can teach a model a desired style, format, or specialized behavior.",
            "Full fine-tuning updates many or all model parameters.",
            "Parameter-efficient fine-tuning updates a smaller set of trainable parameters."
        ],
        "good": [
            "Fine-tuning adapts a pretrained model by continuing training on data representing a target task, domain, or behavior.",
            "Full fine-tuning can update the model's weights broadly, while methods such as LoRA train a much smaller set of additional parameters.",
            "The quality and diversity of fine-tuning data strongly affect the resulting behavior.",
            "Fine-tuning is different from RAG: fine-tuning changes parameters, while RAG supplies external information through the model's context at inference time."
        ],
        "excellent": [
            "Fine-tuning starts from pretrained parameters and optimizes them, or additional adapter parameters, using a target-specific objective. It can specialize behavior, formatting, terminology, or task performance.",
            "Parameter-efficient methods such as LoRA introduce trainable low-rank updates while keeping most base-model parameters frozen. This reduces storage and computational requirements compared with full fine-tuning.",
            "Fine-tuning is not a reliable mechanism for frequently changing factual knowledge. For dynamic or document-specific information, retrieval or tool use can provide fresher grounding without modifying model weights.",
            "Fine-tuning data should represent the desired behavior carefully because the model can learn unwanted patterns, formatting artifacts, or biases present in the training examples."
        ]
    },

    {
        "question": "What is hallucination in an LLM?",
        "topic": "generative_ai",
        "concepts": ["hallucination", "factuality", "llm"],
        "incorrect": [
            "Hallucination means the model has become conscious.",
            "It only happens when an LLM generates images.",
            "A hallucination is always a deliberate lie.",
            "Hallucinations mean the model has no parameters."
        ],
        "weak": [
            "Hallucination means the model gives incorrect information.",
            "LLMs can generate plausible but false statements.",
            "It is a problem in many AI applications.",
            "Grounding can help reduce hallucinations."
        ],
        "partial": [
            "An LLM hallucination is an output that appears plausible but is unsupported or factually incorrect.",
            "Language models optimize predictive objectives rather than guaranteeing factual correctness.",
            "Retrieval, tools, verification, and constrained generation can reduce some hallucinations.",
            "Hallucination can occur even when the generated text sounds confident."
        ],
        "good": [
            "Hallucination refers to generated content that is unsupported, fabricated, or factually incorrect despite appearing plausible.",
            "Because an LLM predicts text rather than directly consulting a guaranteed truth source, it can produce confident answers that are not grounded in evidence.",
            "RAG can reduce hallucination for knowledge-based questions by supplying relevant source material, but retrieval quality and model interpretation still matter.",
            "For high-stakes applications, generated claims should be validated using trusted sources, deterministic checks, or external tools where appropriate."
        ],
        "excellent": [
            "LLM hallucination is a failure mode in which generated content is not adequately supported by the available evidence or is factually false. Fluency and confidence are not reliable indicators of correctness.",
            "Autoregressive language modeling optimizes likelihood of token sequences rather than a formal guarantee of truth. Consequently, the model can generate plausible continuations even when it lacks sufficient evidence.",
            "Grounded generation can reduce hallucination by retrieving authoritative context and requiring answers to rely on it, but it does not eliminate the problem because retrieval can fail and the model can misinterpret or ignore retrieved evidence.",
            "Production systems can combine retrieval, citations, structured outputs, tool calls, validation rules, and human review depending on the consequences of incorrect information."
        ]
    },

    {
        "question": "What is zero-shot prompting?",
        "topic": "generative_ai",
        "concepts": ["zero-shot", "prompting", "llm"],
        "incorrect": [
            "Zero-shot means the model has never been pretrained.",
            "It means giving the model exactly zero input tokens.",
            "Zero-shot prompting requires retraining the model.",
            "It can only be used for mathematics."
        ],
        "weak": [
            "Zero-shot means asking the model to perform a task without examples.",
            "The prompt gives instructions but no demonstrations.",
            "It relies on the model's pretrained capabilities.",
            "It can be used for many tasks."
        ],
        "partial": [
            "Zero-shot prompting asks a pretrained model to perform a task using instructions without task-specific examples in the prompt.",
            "The model must infer the requested behavior from the instruction and its existing training.",
            "For example, asking an LLM to classify a sentence with category definitions but no examples is zero-shot prompting.",
            "It differs from few-shot prompting, which includes demonstrations."
        ],
        "good": [
            "Zero-shot prompting provides a task instruction without giving example input-output demonstrations. The model relies on its pretrained knowledge and instruction-following ability.",
            "A zero-shot prompt can still contain detailed instructions, constraints, context, and an output format; 'zero-shot' specifically refers to the absence of demonstrations for that task.",
            "Few-shot prompting adds examples, while zero-shot prompting does not.",
            "Zero-shot performance depends strongly on the model's pretraining and instruction tuning."
        ],
        "excellent": [
            "Zero-shot prompting means asking a model to perform a task without providing task-specific demonstrations in the prompt. It does not mean the model received zero training; the model is typically extensively pretrained and possibly instruction-tuned.",
            "The prompt can contain definitions, constraints, background information, and a required output schema while still being zero-shot as long as it does not demonstrate input-output examples for the target task.",
            "Zero-shot behavior is useful when prompt length must remain small or when creating demonstrations is expensive, but few-shot examples can improve performance when the desired task format is ambiguous.",
            "Performance depends on the model's learned capabilities and the clarity of the instruction. Zero-shot prompting is therefore an inference-time technique rather than a training method."
        ]
    },

    {
        "question": "What is few-shot prompting?",
        "topic": "generative_ai",
        "concepts": ["few-shot", "prompting", "examples"],
        "incorrect": [
            "Few-shot means training a model with only one parameter.",
            "It means removing examples from the prompt.",
            "Few-shot prompting requires changing the model architecture.",
            "It is only used for image classification."
        ],
        "weak": [
            "Few-shot prompting includes examples in the prompt.",
            "The examples show the model what to do.",
            "It can improve task understanding.",
            "The model does not necessarily get retrained."
        ],
        "partial": [
            "Few-shot prompting provides several input-output examples before the new task input.",
            "The examples demonstrate the desired task and output format.",
            "The model uses these examples as context during inference.",
            "Few-shot prompting changes the prompt rather than permanently changing model weights."
        ],
        "good": [
            "Few-shot prompting gives an LLM a small number of demonstrations showing how inputs should map to desired outputs.",
            "The demonstrations can clarify labels, formatting, reasoning patterns, or task-specific conventions without updating model parameters.",
            "Few-shot prompting can improve performance when instructions alone are ambiguous, but examples consume context-window space.",
            "The quality and consistency of examples matter because the model may imitate undesirable patterns in the demonstrations."
        ],
        "excellent": [
            "Few-shot prompting is an in-context learning technique in which demonstrations are included in the inference context. The model conditions its next output on those examples without performing gradient updates.",
            "Examples can establish a task definition more precisely than prose alone, especially for classification labels, structured output, or domain-specific formatting.",
            "Few-shot demonstrations consume context and can introduce example-specific biases. The number, ordering, diversity, and quality of demonstrations can therefore influence performance.",
            "Unlike fine-tuning, few-shot prompting does not modify persistent model parameters. Its effect is temporary and applies to the particular inference context in which the examples are provided."
        ]
    },

    {
        "question": "What is structured output from an LLM?",
        "topic": "generative_ai",
        "concepts": ["structured-output", "json", "validation"],
        "incorrect": [
            "Structured output means the model can only answer with one word.",
            "It guarantees that every generated fact is correct.",
            "Structured output cannot contain text.",
            "It means the model's weights are stored in JSON."
        ],
        "weak": [
            "Structured output means returning data in a fixed format.",
            "JSON is a common structured format.",
            "It helps programs process model responses.",
            "Schemas can define expected fields."
        ],
        "partial": [
            "Structured output asks an LLM to produce data following a specified schema.",
            "A JSON object can contain fields such as score, feedback, and category.",
            "Validation can check whether the response matches the expected structure.",
            "Structured output makes integration with backend code more reliable."
        ],
        "good": [
            "Structured output constrains an LLM response to a predefined machine-readable format such as JSON with specified fields and types.",
            "A schema can define required properties, allowed values, and data types, making it easier for application code to consume the response.",
            "Schema validation should still be used because correct syntax does not guarantee correct meaning or factual content.",
            "Structured outputs are particularly useful for extraction, classification, tool calls, and application workflows."
        ],
        "excellent": [
            "Structured output provides a contract between the language model and the application, specifying the expected fields, types, and sometimes enumerated values. This reduces ambiguity when model output is consumed programmatically.",
            "A valid JSON response can still contain invalid business logic or unsupported claims, so syntactic validation should be separated from semantic validation.",
            "Schema-constrained generation can be more reliable than asking the model to 'please return JSON,' because the serving system may enforce or guide the output structure during decoding.",
            "In an AI application, structured output can connect an LLM to deterministic code: for example, the model can return an evaluation object containing a score and feedback, after which the application validates ranges and applies business rules."
        ]
    },

    {
        "question": "What is inference in machine learning?",
        "topic": "generative_ai",
        "concepts": ["inference", "prediction", "deployment"],
        "incorrect": [
            "Inference means training a model from scratch.",
            "Inference deletes model parameters.",
            "It only occurs during dataset collection.",
            "Inference is another name for backpropagation."
        ],
        "weak": [
            "Inference means using a trained model.",
            "The model produces predictions during inference.",
            "It happens after or separately from training.",
            "LLMs perform inference when generating text."
        ],
        "partial": [
            "Inference is the process of applying a trained model to new input to produce predictions or generated outputs.",
            "During inference, model parameters are generally not updated.",
            "For an LLM, inference involves processing a prompt and generating output tokens.",
            "Inference speed and memory usage are important deployment considerations."
        ],
        "good": [
            "Inference is the execution of a trained model on input data to obtain predictions, classifications, embeddings, or generated outputs.",
            "Unlike training, normal inference does not update model parameters through gradient descent.",
            "LLM inference includes a forward pass and, for generation, repeated decoding steps to produce tokens.",
            "Techniques such as quantization, batching, caching, and optimized runtimes can improve inference efficiency."
        ],
        "excellent": [
            "Inference is the forward execution of learned parameters on new input. In ordinary deployment, gradients are not calculated for parameter updates, so inference is distinct from the training optimization loop.",
            "For autoregressive LLM generation, the model performs repeated next-token predictions. KV caching can reuse previous attention key-value states, reducing redundant computation as the sequence grows.",
            "Inference performance depends on model size, sequence length, batch size, hardware, precision, memory bandwidth, and serving architecture. Latency and throughput can therefore trade off against each other.",
            "Quantization reduces numerical precision used for model weights or activations and can lower memory requirements and improve serving efficiency, although excessive quantization can reduce model quality."
        ]
    },


    # ============================================================
    # RAG — 10 QUESTIONS
    # ============================================================

    {
        "question": "What is RAG?",
        "topic": "rag",
        "concepts": ["rag", "retrieval", "generation"],
        "incorrect": [
            "RAG is a programming language.",
            "RAG means retraining an LLM every time a user asks a question.",
            "RAG removes documents before generating answers.",
            "RAG is only used for image editing."
        ],
        "weak": [
            "RAG stands for Retrieval-Augmented Generation.",
            "It retrieves information before generating an answer.",
            "RAG can use external documents.",
            "It helps ground an LLM."
        ],
        "partial": [
            "RAG retrieves relevant documents or passages and provides them to an LLM as context for generation.",
            "It can allow a model to answer using information that is not stored directly in its parameters.",
            "A typical RAG pipeline includes document ingestion, chunking, embeddings, retrieval, and generation.",
            "RAG can reduce unsupported answers when retrieval and grounding work well."
        ],
        "good": [
            "Retrieval-Augmented Generation combines information retrieval with an LLM. Relevant passages are retrieved from an external knowledge source and included in the model context before generating an answer.",
            "A common RAG system converts documents into chunks, embeds them into vectors, indexes them, retrieves relevant chunks for a query, and passes those chunks to the language model.",
            "RAG is useful for private, domain-specific, or frequently changing information because the knowledge source can be updated without retraining the base LLM.",
            "RAG quality depends on both retrieval quality and generation quality; a strong LLM cannot reliably answer from information that was not retrieved or otherwise provided."
        ],
        "excellent": [
            "RAG is an architecture that separates knowledge retrieval from language generation. At query time, a retriever selects relevant external content and the generator conditions its response on that evidence.",
            "A typical pipeline includes document parsing, chunking, embedding, vector or lexical indexing, query retrieval, optional reranking, context construction, and grounded generation. Each stage can introduce errors.",
            "RAG is particularly useful when knowledge changes frequently or contains private documents because the retrieval index can be updated independently of the language model's parameters.",
            "RAG does not automatically eliminate hallucination. Poor chunking, weak embeddings, incorrect retrieval, context overload, or model misinterpretation can still produce unsupported answers, so retrieval and answer quality should be evaluated separately."
        ]
    },

    {
        "question": "What is a vector database?",
        "topic": "rag",
        "concepts": ["vector-database", "embeddings", "similarity-search"],
        "incorrect": [
            "A vector database stores only images.",
            "It stores vectors as physical arrows.",
            "A vector database cannot perform search.",
            "It is identical to a spreadsheet."
        ],
        "weak": [
            "A vector database stores embeddings.",
            "It can search for similar vectors.",
            "RAG systems often use vector stores.",
            "Similarity is important in vector search."
        ],
        "partial": [
            "A vector database indexes numerical embedding vectors for similarity search.",
            "A query can be embedded and compared with stored document embeddings.",
            "The database can return the nearest vectors according to a similarity metric.",
            "Vector stores may also keep metadata associated with each vector."
        ],
        "good": [
            "A vector database stores embeddings and provides efficient approximate or exact nearest-neighbor search. It is commonly used to retrieve semantically similar documents in RAG systems.",
            "A text query is converted into an embedding and compared with stored document embeddings using a metric such as cosine similarity or dot product.",
            "Metadata filtering can be combined with vector similarity to restrict retrieval to relevant documents or categories.",
            "Popular vector indexes use structures such as HNSW or inverted-file-based methods to improve search efficiency for large collections."
        ],
        "excellent": [
            "A vector database or vector index is designed to store high-dimensional representations and efficiently retrieve vectors close to a query according to a chosen similarity or distance function.",
            "Approximate nearest-neighbor algorithms such as HNSW trade a small amount of exactness for substantially faster search at scale. The appropriate index depends on dataset size, dimensionality, latency requirements, and update patterns.",
            "In RAG, the vector itself is not the final knowledge. It points to an associated chunk or document, usually through metadata or an identifier, which must then be retrieved and supplied to the language model.",
            "Vector search can be combined with keyword search, metadata filtering, and reranking. Hybrid retrieval is often useful when exact terms and semantic similarity both matter."
        ]
    },

    {
        "question": "What are embeddings in RAG?",
        "topic": "rag",
        "concepts": ["embeddings", "semantic-search", "rag"],
        "incorrect": [
            "RAG embeddings are the original PDF pages.",
            "An embedding is always a single number.",
            "Embeddings contain the complete LLM output.",
            "Embeddings eliminate the need for documents."
        ],
        "weak": [
            "Embeddings represent text as vectors.",
            "They help compare semantic similarity.",
            "Documents and queries can be embedded.",
            "RAG often stores document embeddings."
        ],
        "partial": [
            "An embedding model converts text into numerical vectors that represent useful semantic information.",
            "RAG can embed document chunks and user queries into the same vector space.",
            "Similarity between vectors can be used to retrieve relevant chunks.",
            "The quality of the embedding model strongly affects semantic retrieval."
        ],
        "good": [
            "In RAG, an embedding model converts document chunks and queries into dense vectors so semantically related content can be retrieved using vector similarity.",
            "The embedding model should generally be appropriate for the language and domain of the documents and queries.",
            "Document embeddings are computed during ingestion, while the query embedding is generated at retrieval time.",
            "The retrieved vectors are used to identify source chunks; the original text is then passed to the LLM as context."
        ],
        "excellent": [
            "RAG embeddings map text into a vector space designed so that relevant pieces of content can be found using similarity. A retrieval system typically embeds documents during indexing and embeds the user query at runtime.",
            "Embedding quality depends on the model's training objective, domain coverage, language support, chunking strategy, and similarity metric. A high-dimensional vector is not automatically a good semantic representation.",
            "The embedding is an index representation, not a replacement for the source text. The system normally stores an identifier and metadata linking each vector back to its original chunk.",
            "Different embedding models can produce incompatible vector spaces, so query and document embeddings used for similarity search generally need to come from compatible models and preprocessing pipelines."
        ]
    },

    {
        "question": "What is chunking in RAG?",
        "topic": "rag",
        "concepts": ["chunking", "documents", "retrieval"],
        "incorrect": [
            "Chunking converts a document into one character.",
            "Chunking means deleting half the document.",
            "Chunk size has no effect on retrieval.",
            "Chunking happens only after generation."
        ],
        "weak": [
            "Chunking splits documents into smaller pieces.",
            "The pieces are used for retrieval.",
            "Chunks are embedded separately.",
            "Chunk size is an important RAG setting."
        ],
        "partial": [
            "Chunking divides long documents into smaller passages that can be indexed and retrieved.",
            "Chunks that are too large may contain unrelated information or exceed context limits.",
            "Chunks that are too small may lose important context.",
            "Overlap can preserve information across chunk boundaries."
        ],
        "good": [
            "Chunking breaks documents into retrieval units before embedding and indexing. The goal is to create chunks that contain enough context to answer questions while remaining focused.",
            "Chunk size and overlap affect retrieval quality. Overlap can prevent important information from being split between two chunks.",
            "Semantic or structure-aware chunking can use headings, paragraphs, sections, or other document boundaries rather than only fixed character counts.",
            "There is no universally optimal chunk size; it depends on document structure, embedding model, retrieval method, and the downstream question-answering task."
        ],
        "excellent": [
            "Chunking determines the units that the retrieval system can return. Good chunks balance semantic completeness against retrieval precision and context cost.",
            "Fixed-size chunking is simple but can split sentences or sections awkwardly. Structure-aware approaches can preserve headings, paragraphs, tables, or other meaningful boundaries, while overlap can maintain continuity across boundaries.",
            "Very large chunks may match a query because of one relevant sentence but then provide the LLM with substantial irrelevant context. Very small chunks can improve precision but remove the surrounding information needed to interpret the relevant statement.",
            "Chunking should be evaluated together with retrieval metrics and answer quality. The best chunking strategy is task-dependent rather than a fixed universal number of tokens."
        ]
    },

    {
        "question": "What is semantic search?",
        "topic": "rag",
        "concepts": ["semantic-search", "embeddings", "retrieval"],
        "incorrect": [
            "Semantic search matches only exact spelling.",
            "It ignores the meaning of a query.",
            "Semantic search cannot use embeddings.",
            "It searches only numerical databases."
        ],
        "weak": [
            "Semantic search finds results based on meaning.",
            "It often uses embeddings.",
            "Similar concepts can match even with different words.",
            "It is useful in RAG."
        ],
        "partial": [
            "Semantic search represents queries and documents as embeddings and retrieves items with similar vector representations.",
            "It can find related text even when the exact words differ.",
            "The embedding model determines how semantic relationships are represented.",
            "Semantic search differs from simple keyword matching."
        ],
        "good": [
            "Semantic search retrieves content based on similarity in a learned representation space rather than requiring exact keyword matches.",
            "For example, a query about automobile maintenance may retrieve a document using the term 'car servicing' if their embeddings are sufficiently similar.",
            "Embedding-based semantic search is useful for RAG because users often phrase questions differently from the source documents.",
            "Keyword and semantic retrieval can be combined when exact terminology is important as well as conceptual similarity."
        ],
        "excellent": [
            "Semantic search uses learned representations to retrieve content according to meaning-related similarity. A query and candidate documents are embedded into a compatible vector space and ranked using a similarity or distance function.",
            "Unlike lexical search, semantic retrieval can connect paraphrases and conceptually related expressions. However, it can also miss exact identifiers, rare names, numbers, or highly specific terminology where lexical matching is valuable.",
            "Embedding similarity is only as good as the representation learned by the embedding model. Domain-specific vocabulary, multilingual text, document structure, and query formulation can all affect retrieval quality.",
            "Hybrid retrieval combines semantic similarity with lexical signals, often followed by reranking, to improve robustness across both conceptual and exact-match information needs."
        ]
    },

    {
        "question": "What is retrieval in a RAG pipeline?",
        "topic": "rag",
        "concepts": ["retrieval", "ranking", "rag"],
        "incorrect": [
            "Retrieval means generating the final answer immediately.",
            "Retrieval deletes irrelevant documents permanently.",
            "Retrieval always returns every document.",
            "It happens only during model training."
        ],
        "weak": [
            "Retrieval finds relevant documents.",
            "It uses a query to search a knowledge base.",
            "The retrieved content is sent to the LLM.",
            "Retrieval is an important RAG step."
        ],
        "partial": [
            "Retrieval selects documents or chunks that are likely to contain information relevant to a query.",
            "A retriever can use vector similarity, keyword matching, or both.",
            "The top retrieved chunks are placed into the generation context.",
            "Retrieval quality strongly affects the final answer."
        ],
        "good": [
            "Retrieval is the stage of a RAG system that searches the indexed knowledge source and selects candidate passages relevant to the user's query.",
            "A retriever can rank candidates using embedding similarity, lexical search, metadata filters, or a combination of signals.",
            "The system usually retrieves only a limited number of chunks so the LLM receives focused context rather than the entire document collection.",
            "Retrieval should be evaluated separately from generation because a correct generator cannot answer reliably if the relevant evidence was not retrieved."
        ],
        "excellent": [
            "Retrieval transforms a user query into a ranked set of evidence candidates. Depending on the architecture, this may involve query embedding, vector nearest-neighbor search, lexical retrieval, metadata filtering, hybrid ranking, and reranking.",
            "The number of retrieved chunks creates a precision-recall trade-off. Too few may omit evidence; too many can introduce irrelevant information and consume context capacity.",
            "A useful RAG evaluation distinguishes retrieval recall from answer correctness. For example, a system may fail because the relevant chunk was never retrieved or because it was retrieved but the generator failed to use it correctly.",
            "Production retrieval pipelines often include metadata filters, rerankers, deduplication, source attribution, and document-level permissions in addition to basic vector similarity."
        ]
    },

    {
        "question": "What is reranking in RAG?",
        "topic": "rag",
        "concepts": ["reranking", "retrieval", "ranking"],
        "incorrect": [
            "Reranking means rewriting the entire document.",
            "It deletes all retrieved results.",
            "Reranking happens before a query exists.",
            "It changes the LLM's weights."
        ],
        "weak": [
            "Reranking reorders retrieved documents.",
            "It can improve retrieval relevance.",
            "A second model may be used.",
            "It usually happens after initial retrieval."
        ],
        "partial": [
            "Reranking takes an initial set of retrieved candidates and scores them again to produce a more relevant ordering.",
            "A cross-encoder can compare a query and passage jointly for more detailed relevance estimation.",
            "Reranking is useful because fast vector retrieval may return approximate candidates.",
            "Only the highest-ranked passages may be sent to the LLM."
        ],
        "good": [
            "Reranking is a second-stage retrieval process that re-evaluates an initial candidate set and places the most relevant passages at the top.",
            "A bi-encoder embedding model can efficiently retrieve many candidates, while a more expensive cross-encoder can then jointly examine each query-passage pair.",
            "This two-stage approach balances retrieval speed with more accurate relevance scoring.",
            "Reranking can improve the quality of context supplied to the LLM without changing the underlying language model."
        ],
        "excellent": [
            "Reranking separates candidate recall from final relevance ordering. A fast first-stage retriever retrieves a broader candidate pool, after which a more expressive scoring model evaluates query-document pairs and selects the strongest evidence.",
            "Cross-encoders can model detailed interactions between query and passage tokens because they process them jointly, but this makes them more computationally expensive than independent embedding-based retrieval.",
            "Reranking is especially useful when the first-stage retriever produces several semantically plausible passages but their exact relevance differs. It can improve the evidence ordering before context construction.",
            "A larger candidate pool can improve recall but increases reranking cost. Therefore candidate count and final context size should be tuned against latency, cost, and answer-quality requirements."
        ]
    },

    {
        "question": "How can RAG work with a PDF resume?",
        "topic": "rag",
        "concepts": ["pdf", "resume", "rag"],
        "incorrect": [
            "RAG can read a PDF without extracting any content.",
            "The resume must be manually typed into the LLM every time.",
            "PDFs cannot be used in RAG systems.",
            "A PDF automatically becomes model weights."
        ],
        "weak": [
            "The PDF can be converted to text and indexed.",
            "The resume can be split into chunks.",
            "Embeddings can represent the chunks.",
            "The retrieved resume information can personalize interview questions."
        ],
        "partial": [
            "A resume PDF can be parsed into text, divided into chunks, embedded, and stored in a vector index.",
            "When interviewing the candidate, the system can retrieve resume passages relevant to the current question.",
            "The retrieved information can be supplied to an LLM so it can generate personalized questions.",
            "The pipeline must handle cases where PDF text extraction is incomplete."
        ],
        "good": [
            "A resume RAG pipeline can extract text from the uploaded PDF, clean and chunk it, generate embeddings for the chunks, and store them in a searchable index.",
            "When a question is generated, the system can retrieve relevant resume sections such as skills, projects, education, or experience and include them in the LLM context.",
            "This allows the interviewer to ask questions grounded in the candidate's actual background instead of using only generic questions.",
            "For scanned resumes, OCR may be required because normal PDF text extraction may not recover text from image-only pages."
        ],
        "excellent": [
            "A practical resume-RAG pipeline begins with PDF parsing and, when necessary, OCR. The extracted content is normalized, divided into semantically useful chunks, embedded, and indexed with metadata such as section or page information.",
            "At interview time, the system can retrieve evidence related to a candidate's project, skill, education, or experience and provide that evidence to the question-generation model. This grounds personalization in the actual resume.",
            "The system should preserve provenance so generated questions can be traced to the resume passages that motivated them. It should also avoid treating absence from a resume as proof that a candidate lacks a skill.",
            "PDF extraction is imperfect: columns, tables, unusual fonts, scanned pages, and images can produce missing or incorrectly ordered text. A robust system should detect extraction failures and use OCR or alternative parsing when appropriate."
        ]
    },

    {
        "question": "What is hybrid retrieval in RAG?",
        "topic": "rag",
        "concepts": ["hybrid-retrieval", "bm25", "vector-search"],
        "incorrect": [
            "Hybrid retrieval uses two LLMs to write the same answer.",
            "It means combining two PDFs into one file.",
            "Hybrid retrieval cannot use keyword search.",
            "It is only useful for image generation."
        ],
        "weak": [
            "Hybrid retrieval combines different search methods.",
            "It can combine keyword and vector search.",
            "This can improve retrieval.",
            "It is useful when exact terms and meaning both matter."
        ],
        "partial": [
            "Hybrid retrieval combines lexical search with semantic vector retrieval.",
            "Keyword methods can find exact terms, while embeddings can find semantically related text.",
            "The results can be merged or reranked before being sent to the LLM.",
            "Hybrid retrieval can be more robust than relying on only one retrieval method."
        ],
        "good": [
            "Hybrid retrieval combines lexical signals, such as BM25, with semantic vector similarity to retrieve relevant documents using both exact terms and conceptual relationships.",
            "Lexical search is useful for identifiers, names, numbers, and exact phrases, while vector search is useful for paraphrases and semantic similarity.",
            "The candidate results can be combined using score fusion or passed to a reranker for final ordering.",
            "Hybrid retrieval is particularly useful in technical and enterprise documents where exact terminology and semantic meaning are both important."
        ],
        "excellent": [
            "Hybrid retrieval combines complementary retrieval signals. Lexical methods such as BM25 reward matching terms and their statistical importance, while embedding retrieval captures learned semantic relationships.",
            "The two result sets can be merged using methods such as reciprocal rank fusion or normalized score combinations, followed by optional reranking.",
            "Hybrid retrieval helps address weaknesses of purely semantic search, which may miss exact identifiers or rare terminology, and purely lexical search, which may miss paraphrases.",
            "For a technical RAG system, hybrid retrieval can be especially valuable because queries may contain both natural-language descriptions and exact tokens such as API names, error messages, class names, or version numbers."
        ]
    },

    {
        "question": "Why is metadata useful in RAG?",
        "topic": "rag",
        "concepts": ["metadata", "filtering", "retrieval"],
        "incorrect": [
            "Metadata replaces the document text completely.",
            "Metadata is only useful for changing font colors.",
            "Metadata prevents vector search from working.",
            "Metadata is the same as the LLM's weights."
        ],
        "weak": [
            "Metadata provides extra information about documents.",
            "It can help filter search results.",
            "A chunk can store page or document information.",
            "Metadata can help with citations."
        ],
        "partial": [
            "Metadata can store attributes such as document name, page number, section, user, date, or topic.",
            "Retrieval can use metadata filters to restrict the search space.",
            "Metadata can help identify where retrieved content came from.",
            "It is useful for access control and source attribution."
        ],
        "good": [
            "Metadata adds structured information to indexed chunks, such as document ID, page, section, date, category, or permissions.",
            "Filters can restrict retrieval to relevant documents or authorized content before or during vector search.",
            "Source metadata allows the application to show citations or page references for generated answers.",
            "Metadata can improve retrieval precision without requiring the embedding model to encode every filtering constraint."
        ],
        "excellent": [
            "Metadata provides structured attributes associated with each retrieval unit. It can support pre-filtering, post-filtering, access control, temporal constraints, document-type selection, and provenance.",
            "For example, a resume RAG system can associate every chunk with the candidate ID, page number, section name, and source file. Retrieval can then be restricted to that candidate's documents.",
            "Metadata should not be confused with semantic content. A vector captures learned representation information, while metadata provides explicit fields that can be queried deterministically.",
            "Good metadata design improves both reliability and observability. It allows systems to explain where context came from, enforce permissions, and debug why a particular document was retrieved."
        ]
    },

    {
        "question": "How do you evaluate a RAG system?",
        "topic": "rag",
        "concepts": ["evaluation", "retrieval", "answer-quality"],
        "incorrect": [
            "RAG evaluation only checks whether the server starts.",
            "A RAG system is successful if it generates long answers.",
            "Only the embedding vector size matters.",
            "Evaluation is unnecessary for RAG."
        ],
        "weak": [
            "RAG can be evaluated by checking retrieved documents and answers.",
            "Retrieval quality is important.",
            "Answer correctness is also important.",
            "Human evaluation can be useful."
        ],
        "partial": [
            "RAG evaluation should measure both retrieval quality and generated-answer quality.",
            "Retrieval metrics can check whether relevant passages were retrieved.",
            "Generation evaluation can check correctness, relevance, groundedness, and completeness.",
            "Human review or labeled test questions can provide useful evaluation data."
        ],
        "good": [
            "A RAG system should be evaluated at multiple levels: retrieval relevance, context recall, answer correctness, groundedness, and response quality.",
            "Retrieval metrics can measure whether the expected evidence appears in the top-k results, while generation evaluation determines whether the final answer correctly uses that evidence.",
            "A test set should contain realistic questions with known supporting documents or expected facts.",
            "Automated metrics can be combined with human evaluation because semantic answer quality is difficult to capture with one metric."
        ],
        "excellent": [
            "RAG evaluation should separate retrieval from generation. Retrieval evaluation can measure whether relevant evidence appears in the candidate set or top-k results, while generation evaluation can assess factual correctness, relevance, completeness, and faithfulness to retrieved evidence.",
            "A useful benchmark contains queries, expected evidence, and appropriate answers or claims. This makes it possible to identify whether failures originate in parsing, chunking, retrieval, reranking, context construction, or generation.",
            "Metrics such as recall@k and precision@k can characterize retrieval, while groundedness or citation-based checks can examine whether claims are supported by retrieved passages. Human review remains valuable for nuanced correctness.",
            "End-to-end evaluation should also include operational metrics such as latency, context length, cost, failure rates, and behavior when the answer is not present in the knowledge base."
        ]
    }

]

QUESTIONS.extend(ADDITIONAL_QUESTIONS)
# ============================================================
# DATASET BUILDER
# ============================================================

def build_dataset():
    dataset = []

    label_groups = [
        ("incorrect", 0),
        ("weak", 1),
        ("partial", 2),
        ("good", 3),
        ("excellent", 4),
    ]

    for item in QUESTIONS:

        for group_name, label in label_groups:

            answers = item[group_name]

            for answer in answers:

                dataset.append(
                    {
                        "question": item["question"],
                        "answer": answer,
                        "label": label,
                        "topic": item["topic"],
                        "concepts": item["concepts"]
                    }
                )

    random.shuffle(dataset)

    return dataset


# ============================================================
# MAIN
# ============================================================

def main():

    dataset = build_dataset()

    os.makedirs(
        os.path.dirname(OUTPUT_PATH),
        exist_ok=True
    )

    with open(
        OUTPUT_PATH,
        "w"
    ) as file:

        json.dump(
            dataset,
            file,
            indent=4
        )

    print("=" * 60)
    print("CUSTOM INTERVIEW DATASET")
    print("=" * 60)

    print(
        "Questions:",
        len(QUESTIONS)
    )

    print(
        "Total examples:",
        len(dataset)
    )

    counts = {
        label: 0
        for label in range(5)
    }

    for item in dataset:
        counts[item["label"]] += 1

    print(
        "Label counts:",
        counts
    )

    print(
        "\nSaved to:",
        OUTPUT_PATH
    )


if __name__ == "__main__":
    main()