# ============================================================
# ADDITIONAL INTERVIEW QUESTIONS
# 60 NEW QUESTIONS
# ============================================================

QUESTIONS = [

    # ========================================================
    # PYTHON — 10 QUESTIONS
    # ========================================================

    {
        "question": "What is a Python set and when would you use it?",
        "topic": "python",
        "concepts": ["set", "uniqueness", "membership"],
        "incorrect": [
            "A set is an ordered list that stores duplicate values.",
            "A set is used only for storing strings.",
            "A set is the same thing as a dictionary with values.",
            "A set guarantees that every element keeps its insertion position."
        ],
        "weak": [
            "A set stores multiple values.",
            "Sets are collections in Python.",
            "You can put values inside a set.",
            "A set is another type of container."
        ],
        "partial": [
            "A set is a collection that normally stores unique elements and is useful when duplicates are not needed.",
            "Sets remove duplicate values and are useful for membership checks.",
            "A Python set contains unique elements and can be used for operations such as checking whether a value exists.",
            "Sets are useful when you want unique items and efficient membership testing."
        ],
        "good": [
            "A set is an unordered collection of unique elements. It is useful for removing duplicates and performing fast membership checks.",
            "Python sets store unique values and support operations such as union, intersection, and difference. They are useful when uniqueness matters.",
            "A set automatically eliminates duplicate elements and provides efficient membership testing. It is commonly used for deduplication.",
            "Sets are mutable collections of unique hashable elements. They are especially useful for membership testing and mathematical set operations."
        ],
        "excellent": [
            "A Python set is a mutable collection of unique hashable elements. Because it is hash-based, membership tests are generally O(1) on average. Sets are useful for deduplication and operations such as union, intersection, and difference.",
            "A set maintains unique elements rather than positional duplicates. Internally it uses hashing, which makes average-case membership lookup efficient. It is therefore useful for deduplication, membership checks, and mathematical set operations.",
            "Python sets contain unique hashable objects and do not provide list-style indexing. Their hash-table implementation gives efficient average membership checks, while operations such as intersection and union make them useful for comparing collections.",
            "Sets are ideal when the important property is uniqueness rather than ordering. They use hashing for efficient membership operations and support union, intersection, difference, and symmetric difference."
        ]
    },

    {
        "question": "What is a Python lambda function?",
        "topic": "python",
        "concepts": ["lambda", "anonymous-function", "functional-programming"],
        "incorrect": [
            "A lambda function is a class constructor.",
            "Lambda functions can only be used to create variables.",
            "A lambda function always contains multiple statements.",
            "Lambda is a Python data type used to store files."
        ],
        "weak": [
            "Lambda is a short function.",
            "It is used to make functions smaller.",
            "Lambda creates a function in Python.",
            "It is another way to write Python code."
        ],
        "partial": [
            "A lambda creates a small anonymous function using a single expression.",
            "Lambda functions are anonymous functions that are useful for short operations.",
            "A lambda function lets you define a small function without giving it a normal name.",
            "Lambda is useful when a simple function is needed temporarily."
        ],
        "good": [
            "A lambda function is a small anonymous function defined with the lambda keyword. It is commonly used with functions such as map, filter, and sorted.",
            "Lambda functions are useful for short one-expression operations where defining a full named function would be unnecessary.",
            "A lambda creates an anonymous function and can accept multiple arguments but contains only one expression whose result is returned.",
            "Lambda is commonly used when a function is needed briefly, such as providing a sorting key or transforming values."
        ],
        "excellent": [
            "A lambda is an anonymous function consisting of parameters followed by a single expression. The expression's value is returned automatically. Lambdas are useful for concise callbacks such as sorting keys, map operations, and filters.",
            "Python lambda expressions provide a compact way to create function objects without defining them with def. They are restricted to one expression, so they are best suited to simple transformations or callbacks.",
            "For example, sorted(items, key=lambda x: x.name) uses a lambda as a callback. The lambda receives an item and returns the value used for sorting. For complex logic, a normal def function is clearer.",
            "A lambda is not fundamentally a different kind of function; it creates a function object using expression syntax. Its main limitation is that its body must be a single expression, making it appropriate for concise operations rather than complex business logic."
        ]
    },

    {
        "question": "What is the difference between *args and **kwargs in Python?",
        "topic": "python",
        "concepts": ["args", "kwargs", "function-arguments"],
        "incorrect": [
            "*args is used for keyword arguments and **kwargs is used for positional arguments.",
            "Both are used only for importing modules.",
            "*args creates classes while **kwargs creates objects.",
            "There is no difference between them."
        ],
        "weak": [
            "They are used to pass many arguments.",
            "*args and **kwargs help with functions.",
            "They allow extra values in a function.",
            "They are special Python arguments."
        ],
        "partial": [
            "*args collects extra positional arguments while **kwargs collects extra keyword arguments.",
            "The star form handles positional values and the double-star form handles named values.",
            "They allow a function to accept a variable number of arguments.",
            "*args produces a tuple of extra positional arguments and **kwargs produces a dictionary of extra keyword arguments."
        ],
        "good": [
            "*args collects additional positional arguments into a tuple, while **kwargs collects additional keyword arguments into a dictionary.",
            "They are useful when a function should accept a flexible number of arguments. Positional extras go into args and named extras go into kwargs.",
            "For a function f(*args, **kwargs), calls such as f(1, 2) place values in args, while f(x=1) places the named value in kwargs.",
            "*args and **kwargs make function interfaces flexible. The first captures positional arguments and the second captures keyword arguments."
        ],
        "excellent": [
            "*args captures an arbitrary number of extra positional arguments as a tuple, whereas **kwargs captures extra keyword arguments as a dictionary. They can also be used for unpacking when calling functions.",
            "For example, def f(*args, **kwargs): gives args as a tuple and kwargs as a dictionary. This is useful for wrappers and APIs that need to forward an unknown number of arguments.",
            "The distinction is positional versus keyword arguments. *args handles values such as f(1, 2, 3), while **kwargs handles named values such as f(a=1, b=2). Both can be forwarded to another function using the same syntax.",
            "Using *args and **kwargs provides flexible function signatures, but they should not be used merely to hide an unclear API. They are particularly useful in decorators, wrappers, and functions that need to pass arguments through unchanged."
        ]
    },

    {
        "question": "What is a Python generator?",
        "topic": "python",
        "concepts": ["generator", "yield", "lazy-evaluation"],
        "incorrect": [
            "A generator always stores every result in memory.",
            "Generators are used only to generate random numbers.",
            "A generator is a database table.",
            "Generators cannot produce multiple values."
        ],
        "weak": [
            "A generator generates values.",
            "It is a special Python function.",
            "Generators are useful for loops.",
            "A generator gives values one by one."
        ],
        "partial": [
            "A generator produces values lazily, usually with yield.",
            "Generators return values one at a time instead of creating the entire collection immediately.",
            "The yield keyword is commonly used to create generators.",
            "Generators can save memory because values are produced when needed."
        ],
        "good": [
            "A generator is an iterator that produces values lazily using yield. It avoids storing the complete sequence in memory.",
            "Generators are useful for processing large datasets because they produce one value at a time rather than constructing the entire result at once.",
            "A function containing yield becomes a generator function. Calling next() resumes it until the next yield.",
            "Generators provide lazy iteration and can be much more memory-efficient than building a large list."
        ],
        "excellent": [
            "A generator produces an iterator whose values are computed lazily. A function using yield pauses at each yield and resumes from that point when next() is called.",
            "Generators are valuable for large or streaming datasets because only the current value needs to be held in memory. A list would normally materialize all results immediately.",
            "A generator function returns a generator object rather than executing all iterations immediately. Each next() call resumes execution until another yield or the function ends.",
            "Generators provide lazy evaluation and are especially useful for pipelines, file processing, and large datasets. They improve memory usage, although they generally cannot be randomly indexed like lists."
        ]
    },

    {
        "question": "What is exception handling in Python?",
        "topic": "python",
        "concepts": ["exceptions", "try", "except"],
        "incorrect": [
            "Exception handling prevents Python from executing any code.",
            "Exceptions are only comments in Python.",
            "try is used to define a database.",
            "except means the program must always stop."
        ],
        "weak": [
            "It handles errors.",
            "Exception handling catches problems.",
            "Python uses try and except for errors.",
            "It prevents some errors."
        ],
        "partial": [
            "Exception handling lets a program respond to runtime errors using try and except.",
            "The try block contains code that may fail and except handles selected exceptions.",
            "Python can catch exceptions so the program can respond instead of immediately crashing.",
            "finally can be used when cleanup should happen whether or not an exception occurs."
        ],
        "good": [
            "Python exception handling uses try, except, else, and finally to handle runtime errors and perform appropriate recovery or cleanup.",
            "Code that may raise an exception is placed in try, while except handles matching exception types. finally is useful for cleanup.",
            "Exception handling allows expected runtime failures to be handled explicitly instead of terminating the program unexpectedly.",
            "Good exception handling catches specific exceptions and provides a meaningful recovery path rather than hiding every possible error."
        ],
        "excellent": [
            "Python exception handling provides structured control over runtime failures. Code that may fail is placed in try, matching exceptions are handled in except, else runs when no exception occurs, and finally is used for cleanup.",
            "It is generally better to catch specific exception types rather than using a broad except. This prevents unrelated programming errors from being silently hidden and makes failures easier to diagnose.",
            "For example, file operations can catch FileNotFoundError and perform a useful fallback while finally can close resources. Context managers are often preferable for resource cleanup.",
            "Exception handling separates normal program flow from error recovery. Good practice is to catch only exceptions that can be meaningfully handled, preserve useful error information, and avoid silently swallowing unexpected failures."
        ]
    },

    {
        "question": "What is list comprehension in Python?",
        "topic": "python",
        "concepts": ["list-comprehension", "iteration", "filtering"],
        "incorrect": [
            "List comprehension is used only to create dictionaries.",
            "It always requires a database.",
            "List comprehensions cannot contain conditions.",
            "A list comprehension is the same as importing a package."
        ],
        "weak": [
            "It is a short way to make a list.",
            "It creates lists using loops.",
            "It is a Python shortcut.",
            "It helps create lists."
        ],
        "partial": [
            "List comprehension creates a list from an iterable using compact expression syntax.",
            "It can transform or filter values while constructing a list.",
            "A condition can be included in a list comprehension.",
            "For example, [x * 2 for x in numbers] creates a list of doubled values."
        ],
        "good": [
            "List comprehension is a concise way to create a list by iterating over an iterable and optionally applying an expression or condition.",
            "It can replace a simple loop used to build a list. For example, [x*x for x in nums if x > 0] squares only positive values.",
            "List comprehensions are convenient for simple transformations and filtering, although normal loops may be clearer for complicated logic.",
            "The general form is [expression for item in iterable if condition], where the condition is optional."
        ],
        "excellent": [
            "A list comprehension combines iteration, transformation, and optional filtering into a compact expression. For example, [x*x for x in nums if x > 0] creates squares only for positive values.",
            "List comprehensions are often clearer than a multi-line accumulation loop for simple operations. They create a new list, so they should not be confused with generators, which evaluate lazily.",
            "The expression is evaluated for each item that passes the optional condition. Nested comprehensions are possible, but excessive nesting can reduce readability and should usually be replaced with normal loops.",
            "List comprehensions provide concise list construction, but they do not automatically make an algorithm more efficient. Their main advantage is expressive syntax; complexity is still determined by the operations being performed."
        ]
    },

    {
        "question": "What is a decorator in Python?",
        "topic": "python",
        "concepts": ["decorator", "higher-order-function", "wrapper"],
        "incorrect": [
            "A decorator changes Python's syntax permanently.",
            "Decorators are used only for styling terminal output.",
            "A decorator is a database decorator table.",
            "Decorators cannot accept functions."
        ],
        "weak": [
            "A decorator adds something to a function.",
            "It modifies functions.",
            "Decorators are special Python functions.",
            "They wrap functions."
        ],
        "partial": [
            "A decorator is a callable that modifies or extends another function's behavior.",
            "Decorators commonly wrap a function with additional logic.",
            "The @ syntax is commonly used to apply decorators.",
            "Decorators are useful for reusable behavior such as logging or authentication."
        ],
        "good": [
            "A decorator is a function that takes another function and returns a modified or wrapped function, allowing behavior to be added without changing the original function's core code.",
            "The @decorator syntax applies a decorator to a function. Common uses include logging, authorization, caching, and timing.",
            "Decorators are based on Python's support for functions as first-class objects. A wrapper can execute additional logic before or after calling the original function.",
            "A decorator provides reusable cross-cutting behavior around functions or classes."
        ],
        "excellent": [
            "A decorator is a callable that receives a function or class and returns a modified callable. It is useful for cross-cutting concerns such as logging, caching, authorization, and instrumentation.",
            "For a function f, a decorator can create wrapper(*args, **kwargs), perform pre-processing, call f, then post-process the result. functools.wraps is commonly used so metadata from the original function is preserved.",
            "The @syntax is syntactic sugar for reassigning a function to the result of a decorator. This makes behavior composition concise while keeping the original function implementation focused.",
            "Decorators are powerful because Python treats functions as objects. They should nevertheless be used carefully because multiple nested decorators can make execution flow harder to understand."
        ]
    },

    {
        "question": "What is the difference between shallow copy and deep copy?",
        "topic": "python",
        "concepts": ["copy", "shallow-copy", "deep-copy"],
        "incorrect": [
            "Deep copy only copies the variable name.",
            "Shallow copy always duplicates every nested object.",
            "Both copies are exactly identical in behavior.",
            "Copying has no effect on nested objects."
        ],
        "weak": [
            "Shallow copy is a smaller copy and deep copy is bigger.",
            "Deep copy copies more data.",
            "They are two ways of copying objects.",
            "Deep copy is usually safer."
        ],
        "partial": [
            "A shallow copy creates a new outer object but can share references to nested objects.",
            "A deep copy recursively copies nested objects so they are not shared with the original.",
            "Changes to nested mutable objects can affect both objects after a shallow copy.",
            "Python's copy module provides copy() and deepcopy() for these operations."
        ],
        "good": [
            "A shallow copy duplicates the outer container but keeps references to nested objects, while a deep copy recursively duplicates nested objects.",
            "If a list contains another mutable list, changing the nested list can affect both shallow copies because the nested object is shared.",
            "copy.copy creates a shallow copy, while copy.deepcopy recursively copies reachable objects.",
            "Deep copying can prevent shared nested state, although it can be more expensive and is not always necessary."
        ],
        "excellent": [
            "A shallow copy creates a new outer object but preserves references to objects contained inside it. A deep copy recursively copies nested objects, producing independent nested state where possible.",
            "For example, copying [[1, 2]] shallowly creates a new outer list but both lists reference the same inner list. deepcopy creates a separate inner list as well.",
            "Deep copying uses recursive copying with mechanisms for handling cycles and shared references. It can be expensive and may not be appropriate for objects containing resources such as files or sockets.",
            "The choice depends on ownership of nested state. Shallow copying is sufficient when nested objects can safely be shared; deep copying is useful when independent mutable state is required."
        ]
    },

    {
        "question": "What is a context manager in Python?",
        "topic": "python",
        "concepts": ["context-manager", "with", "resource-management"],
        "incorrect": [
            "A context manager manages Python modules.",
            "The with statement is used only for loops.",
            "Context managers cannot release resources.",
            "A context manager is a type of list."
        ],
        "weak": [
            "It manages resources.",
            "It uses with.",
            "Context managers make code safer.",
            "They help open and close things."
        ],
        "partial": [
            "A context manager controls setup and cleanup around a block of code.",
            "The with statement is commonly used with context managers.",
            "Files are often handled using with so they are closed automatically.",
            "Context managers help ensure cleanup happens even if an exception occurs."
        ],
        "good": [
            "A context manager defines setup and cleanup behavior around a block, commonly used through the with statement.",
            "The with open(...) pattern ensures a file is closed when the block finishes, including when an exception occurs.",
            "Context managers implement the __enter__ and __exit__ protocol or can be created with contextlib.",
            "They are useful for reliable management of resources such as files, locks, and database connections."
        ],
        "excellent": [
            "A context manager controls resource acquisition and release around a block of code. The with statement calls __enter__ before the block and __exit__ afterward, including during exception handling.",
            "For example, with open('file.txt') as f: ensures the file is closed when the block exits. This avoids relying on the programmer to remember explicit cleanup.",
            "Context managers can be implemented with __enter__ and __exit__, or conveniently with contextlib.contextmanager. The exit method can also influence exception propagation.",
            "Context managers provide deterministic cleanup and are useful for files, locks, transactions, network resources, and other objects that require paired setup and teardown operations."
        ]
    },

    {
        "question": "What is the GIL in CPython?",
        "topic": "python",
        "concepts": ["gil", "threads", "concurrency"],
        "incorrect": [
            "GIL means Python can run unlimited CPU threads in one process.",
            "The GIL is a database lock.",
            "The GIL only controls variable names.",
            "The GIL makes multiprocessing impossible."
        ],
        "weak": [
            "GIL is related to threads.",
            "It is a Python lock.",
            "It affects Python performance.",
            "GIL controls execution."
        ],
        "partial": [
            "The Global Interpreter Lock is a mechanism in CPython that restricts execution of Python bytecode by multiple threads at the same time.",
            "The GIL can limit CPU-bound multithreading in CPython.",
            "Threads can still be useful for I/O-bound work despite the GIL.",
            "Multiprocessing can be used to achieve parallel CPU execution across processes."
        ],
        "good": [
            "The CPython GIL allows only one thread at a time to execute Python bytecode within a process, which limits CPU-bound parallelism using threads.",
            "The GIL is less problematic for I/O-bound applications because threads can release execution while waiting for external operations.",
            "For CPU-heavy workloads, multiprocessing or native code that releases the GIL can provide better parallelism.",
            "The GIL is specific to CPython's traditional execution model and should not be treated as a universal Python language rule."
        ],
        "excellent": [
            "In traditional CPython implementations, the Global Interpreter Lock protects interpreter state by allowing only one thread at a time to execute Python bytecode in a process. This limits CPU-bound parallelism with threads.",
            "The GIL does not mean Python cannot perform concurrent I/O. Threads can overlap operations while waiting on I/O, and extensions can release the lock during native work.",
            "For CPU-bound workloads, multiple processes can achieve parallelism because each process has its own interpreter and GIL. Native extensions that release the GIL can also execute computational work concurrently.",
            "The GIL is an implementation detail rather than a property of Python syntax itself. Its behavior and significance depend on the Python implementation and version."
        ]
    },

    # ========================================================
    # MACHINE LEARNING — 10 QUESTIONS
    # ========================================================

    {
        "question": "What is overfitting in machine learning?",
        "topic": "machine-learning",
        "concepts": ["overfitting", "generalization", "validation"],
        "incorrect": [
            "Overfitting means the model performs poorly on both training and test data.",
            "Overfitting happens when the dataset has no features.",
            "Overfitting means the model has learned nothing.",
            "Overfitting always means the model is too small."
        ],
        "weak": [
            "Overfitting is when a model learns too much.",
            "It happens when the model memorizes data.",
            "The model becomes too complex.",
            "Overfitting is a bad training problem."
        ],
        "partial": [
            "Overfitting occurs when a model performs very well on training data but poorly on unseen data.",
            "An overfit model captures noise or patterns that do not generalize.",
            "Regularization and more data can help reduce overfitting.",
            "A large gap between training and validation performance can indicate overfitting."
        ],
        "good": [
            "Overfitting occurs when a model learns training-specific patterns, including noise, and therefore performs worse on unseen data.",
            "Common ways to reduce overfitting include regularization, dropout, early stopping, data augmentation, simpler models, and collecting more training data.",
            "A model that has very high training accuracy but substantially lower validation accuracy may be overfitting.",
            "Overfitting reflects poor generalization rather than simply high model complexity."
        ],
        "excellent": [
            "Overfitting occurs when a model fits the training distribution too closely, including noise or accidental correlations, so its generalization to unseen examples deteriorates. A common symptom is a widening gap between training and validation performance.",
            "Techniques such as L1/L2 regularization, dropout, early stopping, data augmentation, reducing model capacity, and increasing diverse training data can improve generalization.",
            "Overfitting should be diagnosed using a validation or test distribution that is independent from training. High training performance alone does not demonstrate that a model is good.",
            "In a Transformer classifier, overfitting can appear when training loss keeps decreasing while validation loss increases. Regularization, better splits, more diverse examples, and early stopping can help."
        ]
    },

    {
        "question": "What is underfitting in machine learning?",
        "topic": "machine-learning",
        "concepts": ["underfitting", "bias", "model-capacity"],
        "incorrect": [
            "Underfitting means the model memorizes every training example.",
            "Underfitting always gives perfect training accuracy.",
            "Underfitting happens only because of too much data.",
            "Underfitting means the test set was removed."
        ],
        "weak": [
            "Underfitting means the model is too weak.",
            "The model does not learn enough.",
            "It happens when the model is simple.",
            "Underfitting is bad accuracy."
        ],
        "partial": [
            "Underfitting occurs when a model is unable to capture important patterns in the data.",
            "An underfit model can perform poorly on both training and validation data.",
            "Increasing model capacity or training longer can sometimes reduce underfitting.",
            "Poor features or excessive regularization can also cause underfitting."
        ],
        "good": [
            "Underfitting occurs when the model has insufficient capacity or training to learn the important patterns, leading to poor training and validation performance.",
            "Possible solutions include increasing model capacity, improving features, reducing excessive regularization, or training for longer.",
            "Unlike overfitting, underfitting is usually associated with high training error rather than a large train-validation gap.",
            "An overly simple model can underfit a complex relationship in the data."
        ],
        "excellent": [
            "Underfitting occurs when a model has not learned enough of the underlying signal, so both training and validation performance remain poor. It can result from insufficient capacity, poor features, excessive regularization, or inadequate training.",
            "A useful diagnostic is to compare training and validation errors. If both are high and similar, the model may be underfitting; if training error is low but validation error is high, overfitting is more likely.",
            "To address underfitting, one can increase model capacity, train longer, improve representations, reduce overly strong regularization, or provide more informative features.",
            "Underfitting and overfitting are generalization problems at opposite ends: underfitting fails to capture enough signal, while overfitting captures training-specific detail that does not transfer."
        ]
    },

    {
        "question": "What is cross-validation?",
        "topic": "machine-learning",
        "concepts": ["cross-validation", "validation", "model-selection"],
        "incorrect": [
            "Cross-validation trains a model without data.",
            "Cross-validation means removing the test set permanently.",
            "Cross-validation is only used for image processing.",
            "Cross-validation guarantees perfect accuracy."
        ],
        "weak": [
            "Cross-validation checks the model multiple times.",
            "It splits data into parts.",
            "It helps evaluate models.",
            "It is another validation method."
        ],
        "partial": [
            "Cross-validation repeatedly splits training data into training and validation portions to estimate model performance.",
            "In k-fold cross-validation, the data is divided into k folds and each fold is used as validation once.",
            "Cross-validation can help with model selection and hyperparameter tuning.",
            "The final test set should remain separate from cross-validation."
        ],
        "good": [
            "In k-fold cross-validation, the training data is divided into k folds. The model trains on k-1 folds and validates on the remaining fold, repeating until every fold has been used for validation.",
            "Cross-validation provides a more stable estimate of generalization than a single validation split, especially with limited data.",
            "It is commonly used for model comparison and hyperparameter selection while keeping the final test set untouched.",
            "Stratified cross-validation can preserve class proportions in classification problems."
        ],
        "excellent": [
            "K-fold cross-validation partitions the available training data into k folds and performs k training-validation cycles, with each fold serving as validation once. The validation metrics are then aggregated.",
            "Cross-validation reduces dependence on one arbitrary validation split and is particularly useful when datasets are small. Stratified k-fold is often preferred for classification because it preserves approximate class proportions.",
            "Hyperparameters should be selected using cross-validation on the training portion, while an untouched test set should be evaluated only after model selection to obtain an unbiased final estimate.",
            "Cross-validation increases computation because the model is trained multiple times. For time-series or grouped data, ordinary random folds can cause leakage, so specialized splitting strategies are needed."
        ]
    },

    {
        "question": "What is data leakage in machine learning?",
        "topic": "machine-learning",
        "concepts": ["data-leakage", "evaluation", "generalization"],
        "incorrect": [
            "Data leakage means the model has no training data.",
            "Leakage always improves real-world performance.",
            "Data leakage is the same as data augmentation.",
            "Leakage only happens with images."
        ],
        "weak": [
            "Data leakage is when data gets exposed.",
            "It is a problem with datasets.",
            "Leakage makes models inaccurate.",
            "It means information leaks."
        ],
        "partial": [
            "Data leakage occurs when information unavailable at prediction time influences training or evaluation.",
            "Using test information during training is a form of leakage.",
            "Leakage can produce unrealistically high validation or test scores.",
            "Preprocessing should usually be fitted only on training data to avoid leakage."
        ],
        "good": [
            "Data leakage occurs when information from outside the intended training information, such as test labels or future data, influences the model during training.",
            "Leakage can make evaluation metrics look excellent while real-world performance is much worse.",
            "A common example is normalizing the entire dataset before splitting, which allows validation statistics to influence training.",
            "Duplicate or near-duplicate samples across train and test sets can also create leakage."
        ],
        "excellent": [
            "Data leakage occurs when information that would not be legitimately available at prediction time influences training or evaluation. It can produce artificially high metrics and misleading conclusions about generalization.",
            "For example, fitting a scaler on the complete dataset before splitting allows validation information to influence the training representation. The scaler should instead be fitted on training data and then applied to validation and test data.",
            "Leakage can also occur through duplicated samples, target-derived features, temporal violations, or selecting hyperparameters using the final test set.",
            "Preventing leakage requires designing the data pipeline around the prediction-time information boundary and keeping evaluation data genuinely independent from model selection."
        ]
    },

    {
        "question": "What is precision in classification?",
        "topic": "machine-learning",
        "concepts": ["precision", "classification", "false-positive"],
        "incorrect": [
            "Precision measures only the number of training epochs.",
            "Precision is the same as dataset size.",
            "Precision counts true negatives only.",
            "Precision is always equal to recall."
        ],
        "weak": [
            "Precision tells how accurate predictions are.",
            "It measures correct predictions.",
            "Precision is an evaluation metric.",
            "It checks model quality."
        ],
        "partial": [
            "Precision is the fraction of predicted positives that are actually positive.",
            "Precision focuses on false positives among positive predictions.",
            "The formula is TP divided by TP plus FP.",
            "High precision means fewer false positive predictions."
        ],
        "good": [
            "Precision = TP / (TP + FP). It measures how many samples predicted as positive are actually positive.",
            "Precision is especially important when false positives are costly.",
            "A model can have high precision but lower recall if it makes very few positive predictions.",
            "For multiclass problems, precision can be computed per class and then averaged."
        ],
        "excellent": [
            "Precision measures the reliability of positive predictions: TP divided by TP plus FP. A high value means that when the classifier predicts the positive class, it is usually correct.",
            "Precision differs from recall. Recall asks how many actual positives were found, while precision asks how many predicted positives were truly positive.",
            "In multiclass classification, precision can be computed one-vs-rest for each class and aggregated using macro, weighted, or micro averaging depending on the evaluation goal.",
            "If false positives are particularly costly, precision may be prioritized. For example, a medical screening system and a spam filter can have different precision-recall tradeoffs depending on the consequences of errors."
        ]
    },

    {
        "question": "What is recall in classification?",
        "topic": "machine-learning",
        "concepts": ["recall", "sensitivity", "false-negative"],
        "incorrect": [
            "Recall measures only model size.",
            "Recall is TP divided by false positives.",
            "Recall is always the same as precision.",
            "Recall measures the number of parameters."
        ],
        "weak": [
            "Recall checks correct predictions.",
            "It is an evaluation metric.",
            "Recall tells how well the model finds things.",
            "It measures positives."
        ],
        "partial": [
            "Recall is the fraction of actual positive examples that the model correctly identifies.",
            "Recall = TP / (TP + FN).",
            "Recall focuses on false negatives.",
            "High recall means the model misses fewer actual positive examples."
        ],
        "good": [
            "Recall measures the proportion of actual positive samples that are correctly predicted as positive, using TP / (TP + FN).",
            "Recall is important when missing a positive case is more costly than producing a false positive.",
            "A model can increase recall by predicting more positives, potentially reducing precision.",
            "Recall is also called sensitivity or true positive rate in binary classification."
        ],
        "excellent": [
            "Recall measures coverage of actual positives: TP divided by TP plus FN. It answers the question, 'Of all truly positive cases, how many did the model find?'",
            "Precision and recall represent different error tradeoffs. Increasing the decision threshold often improves precision but can reduce recall, while lowering it can increase recall at the cost of more false positives.",
            "For multiclass classification, recall can be calculated independently for each class and aggregated with macro or weighted averaging.",
            "Recall is particularly important when false negatives are expensive, such as detecting rare failures or identifying potentially fraudulent transactions."
        ]
    },

    {
        "question": "What is the F1 score?",
        "topic": "machine-learning",
        "concepts": ["f1", "precision", "recall"],
        "incorrect": [
            "F1 is the number of training layers.",
            "F1 is calculated by adding precision and recall.",
            "F1 ignores both precision and recall.",
            "F1 is always 100 percent."
        ],
        "weak": [
            "F1 combines two metrics.",
            "It is an accuracy metric.",
            "F1 checks model performance.",
            "It uses precision and recall."
        ],
        "partial": [
            "F1 is the harmonic mean of precision and recall.",
            "The formula is 2PR divided by P plus R.",
            "F1 is useful when both precision and recall matter.",
            "A high F1 requires both precision and recall to be reasonably high."
        ],
        "good": [
            "The F1 score is the harmonic mean of precision and recall: 2PR/(P+R). It balances the two metrics.",
            "F1 is useful when a classifier needs both good precision and good recall, especially when classes are imbalanced.",
            "Because it is a harmonic mean, a very low precision or recall strongly reduces the F1 score.",
            "For multiclass tasks, macro F1 calculates F1 for each class and averages them equally."
        ],
        "excellent": [
            "F1 is the harmonic mean of precision and recall, F1 = 2PR/(P+R). Unlike an arithmetic mean, the harmonic mean penalizes situations where one of the two values is substantially lower.",
            "F1 is useful when both false positives and false negatives matter and accuracy may be misleading due to class imbalance.",
            "Macro F1 computes an F1 score independently for each class and averages them equally, making it useful when every class matters equally. Weighted F1 accounts for class frequency.",
            "F1 does not directly incorporate true negatives, so it should be interpreted alongside other metrics when true-negative performance is important."
        ]
    },

    {
        "question": "What is a confusion matrix?",
        "topic": "machine-learning",
        "concepts": ["confusion-matrix", "classification", "errors"],
        "incorrect": [
            "A confusion matrix stores only model weights.",
            "It measures GPU memory.",
            "It is a neural network layer.",
            "It contains only training loss."
        ],
        "weak": [
            "It shows predictions.",
            "A confusion matrix is a table.",
            "It checks classification results.",
            "It shows correct and wrong predictions."
        ],
        "partial": [
            "A confusion matrix compares actual classes with predicted classes.",
            "The diagonal usually represents correct predictions and off-diagonal entries represent classification errors.",
            "It helps identify which classes are being confused.",
            "Precision, recall, and other metrics can be derived from confusion matrix counts."
        ],
        "good": [
            "A confusion matrix is a table where rows and columns represent actual and predicted classes. The diagonal contains correct predictions, while off-diagonal cells show errors.",
            "It is particularly useful for multiclass classification because it shows which specific classes the model confuses.",
            "For binary classification, it contains true positives, true negatives, false positives, and false negatives.",
            "A confusion matrix can reveal systematic errors that overall accuracy hides."
        ],
        "excellent": [
            "A confusion matrix summarizes classification outcomes by cross-tabulating actual labels against predicted labels. Correct predictions normally appear on the diagonal, while off-diagonal cells reveal specific error patterns.",
            "For a five-class answer-quality classifier, the matrix can show whether the model confuses adjacent quality levels such as 'good' and 'excellent' more often than distant classes.",
            "From binary confusion-matrix counts we derive precision, recall, specificity, and related metrics. In multiclass settings, metrics can be computed per class using one-vs-rest interpretations.",
            "A confusion matrix is valuable for diagnosis because two models with identical accuracy can have very different error distributions across classes."
        ]
    },

    {
        "question": "What is regularization in machine learning?",
        "topic": "machine-learning",
        "concepts": ["regularization", "l1", "l2"],
        "incorrect": [
            "Regularization always increases model complexity.",
            "Regularization removes the training dataset.",
            "Regularization guarantees zero error.",
            "Regularization is only used to increase learning rate."
        ],
        "weak": [
            "Regularization prevents overfitting.",
            "It makes the model simpler.",
            "It is used during training.",
            "It controls model behavior."
        ],
        "partial": [
            "Regularization adds a penalty or constraint that discourages overly complex models.",
            "L1 and L2 are common regularization methods.",
            "Regularization can improve generalization.",
            "Too much regularization can cause underfitting."
        ],
        "good": [
            "Regularization reduces overfitting by discouraging overly complex parameter configurations. L1 encourages sparsity while L2 penalizes large weights.",
            "The regularization strength controls the trade-off between fitting the training data and keeping the model constrained.",
            "Weight decay is commonly used as an L2-like regularization method in neural network optimization.",
            "Regularization can improve validation performance but excessive regularization may cause underfitting."
        ],
        "excellent": [
            "Regularization incorporates a preference for simpler or constrained models into optimization. L1 adds a penalty proportional to absolute parameter values and can encourage sparsity, while L2 penalizes squared magnitudes and discourages large weights.",
            "In neural networks, dropout, weight decay, and other techniques can act as regularizers. Their goal is not to improve training accuracy directly but to improve generalization.",
            "The regularization coefficient controls the strength of the constraint. Too little may leave the model overfit, while too much can prevent it from learning useful signal and cause underfitting.",
            "Regularization should be evaluated using validation performance rather than assumed to be beneficial. Its appropriate strength depends on model capacity, dataset size, noise, and task difficulty."
        ]
    },

    {
        "question": "What is gradient descent?",
        "topic": "machine-learning",
        "concepts": ["gradient-descent", "optimization", "learning-rate"],
        "incorrect": [
            "Gradient descent increases the loss intentionally.",
            "It does not use gradients.",
            "Gradient descent only sorts datasets.",
            "It changes labels instead of parameters."
        ],
        "weak": [
            "Gradient descent trains the model.",
            "It reduces loss.",
            "It changes weights.",
            "It is an optimization algorithm."
        ],
        "partial": [
            "Gradient descent updates model parameters in the direction that reduces the loss.",
            "It uses the gradient of the loss with respect to parameters.",
            "The learning rate controls the size of parameter updates.",
            "Repeated updates can move the model toward a local or global minimum depending on the problem."
        ],
        "good": [
            "Gradient descent computes the gradient of the loss with respect to model parameters and updates the parameters in the opposite direction of the gradient.",
            "The learning rate controls how large each update is. Too large can make training unstable, while too small can make it slow.",
            "Stochastic and mini-batch gradient descent estimate gradients using subsets of training data.",
            "Backpropagation calculates gradients in neural networks, while an optimizer such as Adam or SGD uses those gradients to update parameters."
        ],
        "excellent": [
            "Gradient descent is an iterative optimization method that updates parameters opposite to the gradient of the loss. If θ represents parameters, the basic update is θ ← θ − η∇L(θ), where η is the learning rate.",
            "Backpropagation computes gradients efficiently through the computational graph, but backpropagation itself is not the parameter-update algorithm. An optimizer uses the resulting gradients to update weights.",
            "Mini-batch gradient descent estimates the gradient using a batch rather than the entire dataset, providing a practical balance between computational efficiency and gradient noise.",
            "Learning rate is a critical hyperparameter. Schedules, momentum, Adam, and adaptive methods can improve optimization, but they do not eliminate the need for sensible learning-rate selection."
        ]
    },

    # ========================================================
    # DEEP LEARNING — 10 QUESTIONS
    # ========================================================

    {
        "question": "What is backpropagation?",
        "topic": "deep-learning",
        "concepts": ["backpropagation", "gradients", "chain-rule"],
        "incorrect": [
            "Backpropagation generates the training dataset.",
            "It directly changes labels.",
            "Backpropagation only performs inference.",
            "It is another name for tokenization."
        ],
        "weak": [
            "Backpropagation trains neural networks.",
            "It calculates errors.",
            "It changes weights.",
            "It sends information backward."
        ],
        "partial": [
            "Backpropagation computes gradients of the loss with respect to neural network parameters using the chain rule.",
            "It propagates error information backward through the network.",
            "The gradients are then used by an optimizer to update parameters.",
            "Backpropagation itself calculates gradients rather than deciding the update rule."
        ],
        "good": [
            "Backpropagation applies the chain rule to efficiently compute gradients of the loss with respect to parameters throughout a neural network.",
            "The forward pass computes predictions and loss, while backpropagation computes gradients backward through the computational graph.",
            "An optimizer such as SGD or Adam then uses these gradients to update the model parameters.",
            "Backpropagation allows deep networks with many layers to be trained efficiently."
        ],
        "excellent": [
            "Backpropagation is an algorithm for computing derivatives of a loss with respect to network parameters by applying the chain rule backward through the computational graph.",
            "During the forward pass, activations and the loss are computed. During the backward pass, gradients flow from the loss toward earlier layers. The optimizer then uses those gradients to update parameters.",
            "Backpropagation is not itself gradient descent. It computes the gradients; an optimization algorithm such as SGD or Adam determines how parameters are updated.",
            "Efficient automatic differentiation systems implement this process by recording operations during the forward pass and traversing the resulting graph in reverse."
        ]
    },

    {
        "question": "What is dropout in neural networks?",
        "topic": "deep-learning",
        "concepts": ["dropout", "regularization", "training"],
        "incorrect": [
            "Dropout permanently deletes neurons from the model.",
            "Dropout is used only during final evaluation.",
            "Dropout guarantees higher training accuracy.",
            "Dropout changes labels randomly."
        ],
        "weak": [
            "Dropout removes some neurons.",
            "It prevents overfitting.",
            "It is a neural network technique.",
            "Dropout makes training harder."
        ],
        "partial": [
            "Dropout randomly disables a subset of activations during training.",
            "It acts as a regularization technique that can reduce overfitting.",
            "The dropped units are not permanently removed.",
            "Dropout is normally disabled during evaluation."
        ],
        "good": [
            "Dropout randomly sets a fraction of activations to zero during training, reducing reliance on specific neurons and acting as a regularizer.",
            "During evaluation, dropout is disabled and the model uses the learned network normally with appropriate scaling handled by the implementation.",
            "Dropout can reduce overfitting but may hurt performance if the dropout rate is too high.",
            "It is commonly used in neural networks when the model has enough capacity to overfit."
        ],
        "excellent": [
            "Dropout is a stochastic regularization technique in which activations are randomly masked during training. This discourages the network from relying too heavily on particular units or feature combinations.",
            "Modern implementations typically use inverted dropout: surviving activations are scaled during training so that no additional scaling is needed during evaluation, where all units are active.",
            "Dropout is not permanent pruning. Different subnetworks are effectively sampled across training steps, which can improve generalization in some settings.",
            "The appropriate dropout rate depends on architecture and dataset. Excessive dropout can cause underfitting, while no regularization can allow a high-capacity model to overfit."
        ]
    },

    {
        "question": "What is batch normalization?",
        "topic": "deep-learning",
        "concepts": ["batch-normalization", "normalization", "training"],
        "incorrect": [
            "Batch normalization removes all batches.",
            "It only normalizes labels.",
            "Batch normalization is a tokenizer.",
            "It guarantees no overfitting."
        ],
        "weak": [
            "It normalizes data in batches.",
            "It helps neural networks train.",
            "It changes activation values.",
            "It is a normalization layer."
        ],
        "partial": [
            "Batch normalization normalizes intermediate activations using statistics computed from a mini-batch during training.",
            "It has learnable scale and shift parameters.",
            "It can make optimization easier and sometimes improve training stability.",
            "Training and inference use batch statistics differently."
        ],
        "good": [
            "Batch normalization normalizes activations using batch mean and variance, followed by learnable scaling and shifting.",
            "During training it uses statistics from the current batch, while during inference it generally uses running estimates collected during training.",
            "Batch normalization can improve optimization stability and allow useful learning rates.",
            "It is common in convolutional networks, although Transformer architectures more commonly use LayerNorm."
        ],
        "excellent": [
            "Batch normalization standardizes intermediate activations using mini-batch statistics and then applies learnable scale and shift parameters. This can improve optimization and training stability.",
            "During training, batch mean and variance are computed from the current mini-batch. During inference, stored running statistics are typically used so predictions do not depend on the current batch.",
            "BatchNorm behaves differently from LayerNorm: BatchNorm normalizes across batch-related dimensions, while LayerNorm normalizes features within an individual example. Transformers commonly use LayerNorm.",
            "Batch normalization can interact with batch size and data distribution, so it is not universally ideal. Small or highly variable batches can make its statistics noisy."
        ]
    },

    {
        "question": "What is an activation function?",
        "topic": "deep-learning",
        "concepts": ["activation", "relu", "nonlinearity"],
        "incorrect": [
            "An activation function only stores labels.",
            "Activation functions remove all nonlinearity.",
            "They are used only before training starts.",
            "An activation function is a dataset."
        ],
        "weak": [
            "It changes neuron output.",
            "Activation functions help neural networks.",
            "ReLU is an activation function.",
            "They are used between layers."
        ],
        "partial": [
            "An activation function applies a nonlinear transformation to a neuron's output.",
            "ReLU, sigmoid, and tanh are examples of activation functions.",
            "Nonlinear activations allow neural networks to model complex relationships.",
            "Without suitable nonlinearities, stacked linear layers remain equivalent to a linear transformation."
        ],
        "good": [
            "Activation functions introduce nonlinearity into neural networks, allowing them to learn complex mappings rather than only linear relationships.",
            "ReLU outputs max(0,x), sigmoid maps values to approximately 0–1, and tanh maps values to approximately -1–1.",
            "GELU is commonly used in Transformer architectures because of its smooth nonlinear behavior.",
            "Choosing an activation affects gradient flow, optimization, and model behavior."
        ],
        "excellent": [
            "Activation functions transform layer outputs nonlinearly, enabling a neural network to represent functions that cannot be expressed by a stack of linear transformations alone.",
            "ReLU is simple and efficient but can produce inactive units for negative inputs. GELU is smooth and commonly used in Transformers, while sigmoid is often used for probabilities in binary outputs.",
            "The activation function affects gradient propagation and optimization. Saturating functions such as sigmoid can produce small gradients in extreme regions, while ReLU-family functions generally provide stronger gradients over useful ranges.",
            "Activation functions should be distinguished from the final output transformation. For example, a hidden Transformer layer may use GELU while a classification head can use raw logits with cross-entropy loss."
        ]
    },

    {
        "question": "What is an embedding in deep learning?",
        "topic": "deep-learning",
        "concepts": ["embedding", "representation", "vector"],
        "incorrect": [
            "An embedding is always a text file.",
            "Embeddings contain only labels.",
            "An embedding must have exactly two dimensions.",
            "Embeddings cannot represent semantic information."
        ],
        "weak": [
            "An embedding is a vector.",
            "It represents data numerically.",
            "Words can have embeddings.",
            "Embeddings are used in AI models."
        ],
        "partial": [
            "An embedding is a learned numerical vector representation of an object such as a word, sentence, or document.",
            "Similar items can have similar embeddings.",
            "Embeddings allow machine learning models to operate on semantic information numerically.",
            "Text embeddings are widely used in semantic search and RAG."
        ],
        "good": [
            "An embedding maps an object such as text into a dense numerical vector that captures useful semantic or contextual information.",
            "Embedding models are trained so that semantically related inputs tend to have useful relationships in vector space.",
            "Sentence embeddings can be compared using measures such as cosine similarity for semantic retrieval.",
            "In RAG, document chunks and queries can be embedded and compared to retrieve relevant information."
        ],
        "excellent": [
            "An embedding is a learned vector representation that maps discrete or structured information into a continuous numerical space. The geometry of that space can encode semantic or task-relevant relationships.",
            "For semantic retrieval, a sentence-transformer can encode both a query and document chunks into vectors. Similarity, often cosine similarity or an inner product, can then rank candidate chunks.",
            "Embeddings are not guaranteed to represent every aspect of meaning. Their usefulness depends on the training objective, model, domain, and similarity function.",
            "In RAG, embeddings are used for retrieval rather than generation: the embedding model finds relevant context, while a language model typically uses that context to generate the final answer."
        ]
    },

    {
        "question": "What is an epoch in neural network training?",
        "topic": "deep-learning",
        "concepts": ["epoch", "batch", "training"],
        "incorrect": [
            "An epoch means one token.",
            "An epoch is the same as one parameter.",
            "An epoch means the model has finished all future training.",
            "An epoch is a type of activation function."
        ],
        "weak": [
            "An epoch is one training cycle.",
            "It means the model trains once.",
            "Epochs repeat training.",
            "It counts training."
        ],
        "partial": [
            "One epoch means the model has processed the entire training dataset once.",
            "A dataset can be divided into batches and processed across one epoch.",
            "Multiple epochs allow the model to repeatedly learn from the training data.",
            "Too many epochs can contribute to overfitting."
        ],
        "good": [
            "An epoch is one complete pass through the training dataset. If the dataset has 1,000 examples and the batch size is 100, roughly 10 batches make one epoch.",
            "Training usually requires multiple epochs so the model can gradually update its parameters.",
            "The number of epochs is a hyperparameter and should be selected using validation performance or early stopping.",
            "An epoch differs from an iteration, where one iteration usually corresponds to one parameter update for one batch."
        ],
        "excellent": [
            "An epoch represents one complete pass through the training dataset. With mini-batch training, the dataset is divided into batches and each batch normally produces one optimizer update.",
            "For N training examples and batch size B, the number of optimizer steps per epoch is approximately ceil(N/B), depending on whether incomplete batches are dropped.",
            "More epochs are not automatically better. Training loss may continue decreasing while validation performance worsens, which is why validation monitoring and early stopping are useful.",
            "Epoch count should be interpreted together with batch size, optimizer, learning rate, dataset size, and model capacity because these factors determine how much optimization occurs."
        ]
    },

    {
        "question": "What is a learning rate?",
        "topic": "deep-learning",
        "concepts": ["learning-rate", "optimization", "gradient"],
        "incorrect": [
            "Learning rate is the number of training examples.",
            "It controls the vocabulary size.",
            "It determines the number of classes.",
            "It is the same as accuracy."
        ],
        "weak": [
            "Learning rate controls training speed.",
            "It tells how much weights change.",
            "It is an optimizer setting.",
            "It affects model learning."
        ],
        "partial": [
            "Learning rate controls the magnitude of parameter updates made by an optimizer.",
            "A very large learning rate can make training unstable.",
            "A very small learning rate can make optimization slow.",
            "Learning-rate schedules can change the value during training."
        ],
        "good": [
            "The learning rate determines how large the optimizer's parameter updates are. It strongly affects convergence and training stability.",
            "If it is too large, the optimizer can overshoot useful regions or diverge; if too small, training can be extremely slow.",
            "Learning-rate schedules such as step decay, cosine decay, or ReduceLROnPlateau can adapt the rate during training.",
            "Learning rate is often one of the most important hyperparameters to tune."
        ],
        "excellent": [
            "The learning rate controls the scale of parameter updates based on the computed gradients. In basic gradient descent, θ is updated as θ − η∇L, where η is the learning rate.",
            "A rate that is too high can cause oscillation or divergence, while one that is too low can lead to slow convergence or poor progress through flat regions.",
            "Schedulers can reduce or otherwise vary the learning rate during training. Adaptive optimizers such as Adam also maintain parameter-specific update statistics, but their global learning-rate setting remains important.",
            "Learning-rate selection interacts with batch size, optimizer, initialization, normalization, and model architecture, so a good value is task- and setup-dependent."
        ]
    },

    {
        "question": "What is transfer learning?",
        "topic": "deep-learning",
        "concepts": ["transfer-learning", "pretraining", "fine-tuning"],
        "incorrect": [
            "Transfer learning means copying files between computers.",
            "It requires training every model from scratch.",
            "Transfer learning cannot use pretrained models.",
            "It is only used for databases."
        ],
        "weak": [
            "Transfer learning uses an existing model.",
            "It saves training time.",
            "A pretrained model is reused.",
            "It helps with small datasets."
        ],
        "partial": [
            "Transfer learning uses knowledge learned from one task or dataset to help solve another task.",
            "A pretrained model can be fine-tuned for a specialized task.",
            "It can reduce training requirements when the target dataset is small.",
            "The transferred representation may need adaptation to the target domain."
        ],
        "good": [
            "Transfer learning starts with a model pretrained on a large dataset and adapts it to a new task, often through fine-tuning or feature extraction.",
            "It is useful when the target dataset is too small to train a large model from scratch.",
            "Fine-tuning updates some or all pretrained parameters using target-task data.",
            "Transfer learning can provide better initialization and generalization than random initialization."
        ],
        "excellent": [
            "Transfer learning reuses representations or parameters learned from a source task to improve learning on a target task. A common approach is to start from a pretrained model and fine-tune it on the target dataset.",
            "With small target datasets, freezing some pretrained layers and training a task-specific head can reduce overfitting and computational cost. With sufficient data, broader fine-tuning can adapt the representation more deeply.",
            "Transfer learning works well when the source and target domains share useful structure, but domain mismatch can limit its benefits or introduce negative transfer.",
            "For an interview evaluator, a pretrained language representation could be adapted to classify answer quality, while a small custom Transformer can demonstrate task-specific architecture and training."
        ]
    },

    {
        "question": "What is vanishing gradient?",
        "topic": "deep-learning",
        "concepts": ["vanishing-gradient", "backpropagation", "optimization"],
        "incorrect": [
            "Vanishing gradients mean the dataset disappears.",
            "It means gradients become infinitely large.",
            "It only happens during inference.",
            "It is caused by increasing the batch size."
        ],
        "weak": [
            "Gradients become too small.",
            "The model stops learning.",
            "It affects deep networks.",
            "Backpropagation has a gradient problem."
        ],
        "partial": [
            "Vanishing gradients occur when gradients become extremely small as they propagate through many layers.",
            "Very small gradients can make earlier layers learn extremely slowly.",
            "Saturating activations and deep chains of derivatives can contribute to the problem.",
            "ReLU-family activations and suitable initialization can help in some architectures."
        ],
        "good": [
            "Vanishing gradients occur when repeated multiplication of derivatives causes gradients to become very small, making early layers difficult to train.",
            "Sigmoid and tanh can saturate and produce small derivatives in certain regions, contributing to the problem.",
            "ReLU-family activations, residual connections, normalization, and careful initialization can improve gradient flow.",
            "The issue is especially important in very deep networks and long recurrent sequences."
        ],
        "excellent": [
            "Vanishing gradients occur when derivatives propagated backward through many operations become progressively smaller, causing early layers or time steps to receive extremely weak learning signals.",
            "For sigmoid or tanh in saturated regions, derivatives can be small, and multiplying many such derivatives can shrink gradients exponentially with depth or sequence length.",
            "Residual connections provide shorter gradient paths, while appropriate normalization, initialization, and non-saturating activations can improve optimization. Transformer architectures also benefit from residual pathways and normalization.",
            "Vanishing gradients differ from exploding gradients, where gradients become excessively large. Both problems can make optimization unstable or ineffective."
        ]
    },

    {
        "question": "What is an optimizer in deep learning?",
        "topic": "deep-learning",
        "concepts": ["optimizer", "adam", "sgd"],
        "incorrect": [
            "An optimizer creates the training labels.",
            "An optimizer only performs inference.",
            "An optimizer replaces the dataset.",
            "Optimizers are activation functions."
        ],
        "weak": [
            "An optimizer trains the model.",
            "It changes weights.",
            "Adam is an optimizer.",
            "It helps reduce loss."
        ],
        "partial": [
            "An optimizer uses gradients to update neural network parameters.",
            "SGD and Adam are common optimizers.",
            "Optimizers determine how parameter updates are performed.",
            "Learning rate is an important optimizer setting."
        ],
        "good": [
            "An optimizer takes gradients computed by backpropagation and updates model parameters to reduce the loss.",
            "SGD directly uses gradients, while Adam maintains moving estimates of gradient and squared-gradient statistics to adapt updates.",
            "Optimizer choice and learning rate can significantly affect convergence.",
            "AdamW is commonly used in Transformer training because it combines Adam-style adaptive updates with decoupled weight decay."
        ],
        "excellent": [
            "An optimizer defines the parameter-update rule used after gradients are computed. SGD uses gradient information directly, while Adam maintains moving estimates of first and second moments to adapt update magnitudes.",
            "AdamW separates weight decay from the adaptive gradient update, making its regularization behavior different from simply adding an L2 term to the loss.",
            "Optimizer choice affects convergence speed, stability, generalization, and memory usage. The learning rate remains a critical hyperparameter even with adaptive optimizers.",
            "Backpropagation and optimization are distinct stages: backpropagation computes derivatives of the loss, while the optimizer uses those derivatives to modify parameters."
        ]
    },

    # ========================================================
    # TRANSFORMERS — 10 QUESTIONS
    # ========================================================

    {
        "question": "What is self-attention?",
        "topic": "transformers",
        "concepts": ["self-attention", "query", "key", "value"],
        "incorrect": [
            "Self-attention only compares the first token with itself.",
            "Self-attention removes all token relationships.",
            "It is a convolution operation.",
            "Self-attention does not use vectors."
        ],
        "weak": [
            "Self-attention lets tokens look at each other.",
            "It finds important words.",
            "Attention connects tokens.",
            "It is part of Transformers."
        ],
        "partial": [
            "Self-attention allows each token to consider other tokens in the same sequence.",
            "It uses query, key, and value representations.",
            "Attention weights determine how much information each token receives from other tokens.",
            "Self-attention helps capture relationships between distant tokens."
        ],
        "good": [
            "Self-attention computes relationships between tokens by comparing queries with keys and using the resulting weights to combine value vectors.",
            "For each token, attention determines which other tokens are relevant to its representation.",
            "The standard attention operation is softmax(QKᵀ/√dₖ)V.",
            "Self-attention allows information to flow directly between tokens regardless of their distance in the sequence."
        ],
        "excellent": [
            "Self-attention represents each token using information from other tokens in the same sequence. Queries are compared with keys to produce attention scores, which are normalized and used to weight value vectors.",
            "The scaled dot-product attention equation is softmax(QKᵀ/√dₖ)V. Scaling by √dₖ helps control the magnitude of dot products before softmax.",
            "Because every token can attend to every other token, self-attention captures long-range dependencies more directly than sequential recurrent processing, although standard full attention has O(n²) pairwise complexity.",
            "Different attention heads can learn different relationships or representation subspaces, which is why Transformers typically use multi-head attention rather than a single attention calculation."
        ]
    },

    {
        "question": "What is multi-head attention?",
        "topic": "transformers",
        "concepts": ["multi-head-attention", "attention-heads", "representation"],
        "incorrect": [
            "Multi-head attention means using multiple datasets.",
            "It repeats the same exact scalar calculation without projections.",
            "It is only used for image resizing.",
            "Multi-head attention removes the attention mechanism."
        ],
        "weak": [
            "It uses many attention heads.",
            "Multiple attentions work together.",
            "It helps Transformers understand text.",
            "Each head looks at information."
        ],
        "partial": [
            "Multi-head attention performs attention in several learned representation subspaces.",
            "Each head has separate query, key, and value projections.",
            "The outputs of the heads are concatenated and projected.",
            "Multiple heads can capture different relationships."
        ],
        "good": [
            "Multi-head attention runs several attention operations with different learned projections, allowing the model to capture different relationships in parallel.",
            "Each head computes attention independently, after which the head outputs are concatenated and passed through an output projection.",
            "Different heads can specialize in different positional or semantic relationships.",
            "Multi-head attention increases representational flexibility compared with a single attention head."
        ],
        "excellent": [
            "Multi-head attention projects the input into multiple query, key, and value subspaces. Each head performs scaled dot-product attention independently, and the resulting representations are concatenated and linearly projected.",
            "Using multiple heads allows different subspaces to represent different relationships, such as local syntax, long-range dependencies, or semantic associations.",
            "If the model dimension is d_model and there are h heads, each head commonly operates on approximately d_model/h dimensions so that the total computational scale remains manageable.",
            "Multi-head attention is one reason Transformers can represent multiple relationships simultaneously rather than forcing every dependency into a single attention distribution."
        ]
    },

    {
        "question": "Why do Transformers need positional encoding?",
        "topic": "transformers",
        "concepts": ["positional-encoding", "sequence-order", "attention"],
        "incorrect": [
            "Positional encoding removes token meaning.",
            "Transformers automatically know exact word order without position information.",
            "It is used to create labels.",
            "Positional encoding is only for images."
        ],
        "weak": [
            "It tells the model word positions.",
            "It adds position information.",
            "It helps with sequence order.",
            "It is added to token embeddings."
        ],
        "partial": [
            "Self-attention alone does not inherently encode token order.",
            "Positional information tells the model where tokens occur in the sequence.",
            "Sinusoidal and learned positional embeddings are common approaches.",
            "Without position information, different token orders could be difficult to distinguish."
        ],
        "good": [
            "Transformers process tokens using attention without requiring sequential recurrence, so positional information must be provided to distinguish token order.",
            "Positional encodings can be learned embeddings or fixed functions such as sinusoidal encodings.",
            "The positional representation is typically combined with token representations before attention.",
            "Modern architectures can also use alternatives such as rotary positional embeddings."
        ],
        "excellent": [
            "Self-attention is largely permutation-equivariant: without positional information, changing the order of tokens would not provide the model with an inherent notion of sequence position. Positional representations solve this problem.",
            "Classic Transformer architectures add positional encodings to token embeddings. Sinusoidal encodings use deterministic sine and cosine functions, while learned positional embeddings are trained parameters.",
            "Modern language models often use rotary positional embeddings or related mechanisms that inject relative positional information directly into attention computations.",
            "Position information is essential because 'dog bites man' and 'man bites dog' contain the same tokens but have different meanings due to their order."
        ]
    },

    {
        "question": "What is a Transformer encoder?",
        "topic": "transformers",
        "concepts": ["encoder", "transformer", "bidirectional"],
        "incorrect": [
            "An encoder only generates audio.",
            "The encoder cannot use attention.",
            "An encoder always predicts one token at a time.",
            "The encoder is a database component."
        ],
        "weak": [
            "The encoder processes input text.",
            "It uses attention.",
            "It understands the input.",
            "It is part of Transformers."
        ],
        "partial": [
            "A Transformer encoder converts an input sequence into contextual representations.",
            "Encoder self-attention can allow tokens to attend to other input tokens.",
            "Encoder representations can be used for classification and other understanding tasks.",
            "BERT is an example of an encoder-based Transformer."
        ],
        "good": [
            "A Transformer encoder processes an input sequence using self-attention and feed-forward layers to produce contextual representations for each token.",
            "Encoder-only models such as BERT are commonly used for understanding tasks such as classification, retrieval, and token labeling.",
            "The encoder can use bidirectional context because each token can attend to tokens on both sides when no causal mask is applied.",
            "Encoder layers typically contain multi-head attention, a feed-forward network, residual connections, and normalization."
        ],
        "excellent": [
            "A Transformer encoder maps an input sequence to contextual hidden representations. In an encoder-only architecture such as BERT, each token can generally attend to both earlier and later tokens because causal masking is not required for the representation task.",
            "A typical encoder layer contains multi-head self-attention followed by a position-wise feed-forward network, with residual connections and normalization around these transformations.",
            "Encoder representations are useful for understanding-oriented tasks such as classification, semantic retrieval, token classification, and extracting contextual features.",
            "Unlike an autoregressive decoder, a standard encoder does not need to generate the sequence one token at a time. It can process the input representations in parallel."
        ]
    },

    {
        "question": "What is a Transformer decoder?",
        "topic": "transformers",
        "concepts": ["decoder", "causal-mask", "generation"],
        "incorrect": [
            "A decoder can only classify images.",
            "A decoder never uses attention.",
            "A decoder always sees future tokens during autoregressive training.",
            "Decoder means converting Python into machine code."
        ],
        "weak": [
            "A decoder generates output.",
            "It predicts tokens.",
            "It uses attention.",
            "It is used in language models."
        ],
        "partial": [
            "A Transformer decoder can generate tokens autoregressively.",
            "Decoder self-attention can use a causal mask to prevent access to future tokens.",
            "Some encoder-decoder architectures also use cross-attention in the decoder.",
            "GPT-style models are decoder-only Transformers."
        ],
        "good": [
            "A Transformer decoder is designed for generating output representations or tokens. In autoregressive language models, causal self-attention prevents a token from attending to future positions.",
            "Decoder-only models such as GPT use masked self-attention to predict the next token from previous tokens.",
            "Encoder-decoder models add cross-attention so the decoder can attend to encoder representations.",
            "Causal masking preserves the left-to-right generation objective."
        ],
        "excellent": [
            "A Transformer decoder supports autoregressive generation by restricting self-attention so each position can only use information from allowed previous positions. This is commonly implemented with a causal mask.",
            "Decoder-only models such as GPT use masked self-attention and predict the next token from the preceding context. Encoder-decoder models additionally use cross-attention to consume representations produced by an encoder.",
            "During training, teacher forcing can provide the shifted target sequence so many positions can be trained in parallel while the causal mask preserves the autoregressive dependency.",
            "The distinction between encoder and decoder is architectural and objective-dependent: encoders are typically optimized for contextual representation, while decoders are commonly used for conditional or autoregressive generation."
        ]
    },

    {
        "question": "What is a Transformer feed-forward network?",
        "topic": "transformers",
        "concepts": ["ffn", "transformer-block", "mlp"],
        "incorrect": [
            "The feed-forward network only stores token IDs.",
            "It replaces attention completely.",
            "It is used only during data loading.",
            "It performs database queries."
        ],
        "weak": [
            "It is another neural network layer.",
            "It processes each token.",
            "It comes after attention.",
            "It helps transform representations."
        ],
        "partial": [
            "The Transformer feed-forward network applies the same small neural network independently to each token position.",
            "It commonly contains two linear layers with a nonlinear activation between them.",
            "The FFN increases and then projects the representation dimension.",
            "It provides nonlinear transformation after attention."
        ],
        "good": [
            "A Transformer feed-forward network is typically a two-layer MLP applied independently and identically to each sequence position, with a nonlinear activation between the layers.",
            "The first linear layer usually expands the hidden dimension and the second projects it back to the model dimension.",
            "Attention mixes information across token positions, while the FFN transforms each position's representation independently.",
            "GELU is a common activation used in Transformer FFNs."
        ],
        "excellent": [
            "The Transformer position-wise feed-forward network is typically an MLP applied independently to each token representation. A common form is Linear → activation → Linear, often expanding d_model to a larger intermediate dimension before projecting back.",
            "Self-attention performs cross-token information mixing, whereas the FFN performs nonlinear feature transformation separately at each position.",
            "Because the same FFN parameters are applied to every position, it is position-wise rather than position-specific. Positional information is handled elsewhere in the architecture.",
            "In many modern Transformers, the FFN is a significant portion of parameter count and computation. Variants such as gated linear units modify its structure while preserving the basic role of nonlinear feature transformation."
        ]
    },

    {
        "question": "What is layer normalization?",
        "topic": "transformers",
        "concepts": ["layer-normalization", "transformers", "normalization"],
        "incorrect": [
            "Layer normalization normalizes the dataset before training only.",
            "It removes entire Transformer layers.",
            "It normalizes labels instead of activations.",
            "LayerNorm is identical to dropout."
        ],
        "weak": [
            "It normalizes neural network values.",
            "LayerNorm helps Transformers.",
            "It keeps values stable.",
            "It is a normalization method."
        ],
        "partial": [
            "Layer normalization normalizes features within an individual example.",
            "It is widely used in Transformer architectures.",
            "LayerNorm typically uses learnable scale and bias parameters.",
            "Unlike BatchNorm, LayerNorm does not depend on batch statistics."
        ],
        "good": [
            "Layer normalization normalizes activations across the feature dimension for each individual token or example, using learned scale and bias.",
            "Transformers commonly use LayerNorm because its behavior does not depend on the batch size or batch statistics.",
            "LayerNorm can improve optimization stability by controlling activation scale.",
            "It differs from BatchNorm, which uses statistics aggregated over a batch."
        ],
        "excellent": [
            "Layer normalization normalizes the features of an individual representation using its mean and variance, followed by learnable scale and bias. It does not require statistics from other examples in the batch.",
            "This makes LayerNorm well suited to variable batch sizes and sequence processing. Transformer blocks commonly use LayerNorm around attention and feed-forward transformations.",
            "BatchNorm and LayerNorm normalize different dimensions and therefore behave differently. BatchNorm relies on batch-level statistics, while LayerNorm computes statistics within each example's feature representation.",
            "Transformer variants differ in whether they use post-normalization or pre-normalization. Pre-norm architectures place normalization before major sublayers and can improve optimization stability for deep networks."
        ]
    },

    {
        "question": "What is autoregressive language modeling?",
        "topic": "transformers",
        "concepts": ["autoregressive", "next-token", "generation"],
        "incorrect": [
            "Autoregressive modeling predicts all tokens without using context.",
            "It predicts only the first token.",
            "It is a type of image compression.",
            "It cannot generate text."
        ],
        "weak": [
            "It predicts the next token.",
            "It generates text step by step.",
            "It uses previous tokens.",
            "GPT uses it."
        ],
        "partial": [
            "Autoregressive language modeling predicts the next token based on previous tokens.",
            "The model generates a sequence one token at a time during inference.",
            "Causal masking prevents the model from seeing future target tokens during training.",
            "GPT-style models commonly use autoregressive objectives."
        ],
        "good": [
            "Autoregressive language models estimate the probability of the next token conditioned on previous tokens, allowing text to be generated sequentially.",
            "During training, causal masking prevents each position from accessing future tokens, while teacher forcing allows many next-token predictions to be computed in parallel.",
            "During generation, the model repeatedly predicts a next-token distribution and appends a selected token to the context.",
            "GPT-style decoder-only Transformers are examples of autoregressive language models."
        ],
        "excellent": [
            "Autoregressive language modeling factorizes sequence probability as a product of conditional next-token probabilities: P(x₁,...,xₙ)=∏P(xᵢ|x₁,...,xᵢ₋₁).",
            "Training can compute many next-token losses in parallel because the causal mask prevents each position from using future tokens. At inference time, however, generated tokens are fed back sequentially.",
            "The generation process involves choosing tokens from the predicted probability distribution using strategies such as greedy decoding, sampling, top-k, or nucleus sampling.",
            "Autoregressive models naturally support open-ended generation but may accumulate errors across long generations because each generated token becomes part of the future context."
        ]
    },

    {
        "question": "What is attention masking?",
        "topic": "transformers",
        "concepts": ["masking", "attention", "padding"],
        "incorrect": [
            "Attention masking increases every attention score.",
            "Masking deletes the model weights.",
            "Masks are only used for image labels.",
            "Attention masking means removing token embeddings permanently."
        ],
        "weak": [
            "Masking hides some tokens.",
            "It controls attention.",
            "It prevents certain tokens from being seen.",
            "Masks are used in Transformers."
        ],
        "partial": [
            "Attention masks prevent attention from being assigned to certain positions.",
            "Padding masks stop the model from attending to padding tokens.",
            "Causal masks prevent attention to future positions.",
            "Masks are usually applied to attention scores before softmax."
        ],
        "good": [
            "Attention masks restrict which positions can contribute to attention. Padding masks ignore padding tokens, while causal masks prevent access to future tokens in autoregressive models.",
            "A mask is commonly applied by adding a very negative value to disallowed attention logits before softmax, making their probabilities approximately zero.",
            "Padding and causal masks solve different problems and can sometimes be combined.",
            "Correct masking is important because otherwise a model may learn from invalid or future information."
        ],
        "excellent": [
            "Attention masking modifies attention logits so that certain key positions receive effectively zero probability after softmax. A padding mask excludes artificial padding positions, while a causal mask enforces autoregressive information flow.",
            "For causal attention, the mask is typically triangular: position i may attend to positions at or before i but not positions after i.",
            "Padding masks depend on the actual sequence lengths within a batch. Without them, padded representations can influence attention and distort the learned representation.",
            "Masking is a form of structural constraint rather than deleting information from the input permanently. The same token can be valid in one attention context and masked in another."
        ]
    },

    {
        "question": "What is softmax in a Transformer?",
        "topic": "transformers",
        "concepts": ["softmax", "attention", "probability"],
        "incorrect": [
            "Softmax converts text directly into PDFs.",
            "Softmax always produces negative probabilities.",
            "Softmax removes all values except the largest.",
            "Softmax is an optimizer."
        ],
        "weak": [
            "Softmax gives probabilities.",
            "It converts numbers into scores.",
            "It is used in attention.",
            "It normalizes values."
        ],
        "partial": [
            "Softmax converts a vector of logits into nonnegative values that sum to one.",
            "It is commonly used to produce attention weights.",
            "Larger logits receive larger probabilities.",
            "Softmax is also used in multiclass classification outputs."
        ],
        "good": [
            "Softmax converts logits into a probability distribution by exponentiating and normalizing them so the outputs sum to one.",
            "In attention, softmax transforms scaled query-key scores into weights used to combine value vectors.",
            "Subtracting the maximum logit before exponentiation is a common numerical-stability technique.",
            "Softmax can become very peaked when logits have large differences."
        ],
        "excellent": [
            "For logits z, softmax produces pᵢ=eᶻⁱ/Σⱼeᶻʲ, creating nonnegative outputs that sum to one. In attention, these values become normalized weights over keys.",
            "Scaled dot-product attention applies softmax to QKᵀ/√dₖ. The scaling reduces the tendency for large dot products to push softmax into extreme saturation.",
            "For numerical stability, implementations commonly subtract max(z) before exponentiation because this leaves the softmax probabilities unchanged while reducing overflow risk.",
            "Softmax should not be confused with the language model's sampling strategy. It produces a probability distribution; temperature, top-k, and top-p may then modify how tokens are sampled from that distribution."
        ]
    },

    # ========================================================
    # LLM / GENERATIVE AI — 10 QUESTIONS
    # ========================================================

    {
        "question": "What is a large language model?",
        "topic": "llm",
        "concepts": ["llm", "language-model", "transformer"],
        "incorrect": [
            "An LLM is a database containing every possible answer.",
            "An LLM is only a search engine.",
            "LLMs cannot generate new text.",
            "An LLM is a traditional spreadsheet."
        ],
        "weak": [
            "An LLM understands language.",
            "It is a big AI model.",
            "It generates text.",
            "It is trained on lots of text."
        ],
        "partial": [
            "An LLM is a neural network trained on large amounts of text to model language patterns.",
            "Many modern LLMs use Transformer architectures.",
            "They can generate, summarize, classify, and transform text.",
            "LLMs generate outputs from learned statistical patterns rather than retrieving every answer from a database."
        ],
        "good": [
            "A large language model is a neural network trained on large-scale text data to model relationships between tokens and generate or transform language.",
            "Modern LLMs commonly use Transformer architectures and are pretrained on next-token prediction or related objectives.",
            "After pretraining, models can be instruction-tuned or aligned for conversational and task-specific behavior.",
            "LLMs can perform many tasks but may hallucinate because generation is based on learned patterns rather than guaranteed factual retrieval."
        ],
        "excellent": [
            "An LLM is a high-capacity neural language model trained to estimate and generate sequences of tokens. Modern LLMs commonly use Transformer architectures and large-scale pretraining objectives such as next-token prediction.",
            "Pretraining learns broad statistical representations from diverse data, while instruction tuning and alignment can adapt the model to follow user requests and behave more helpfully.",
            "LLMs do not function as deterministic databases of facts. Their outputs are generated from learned representations and probability distributions, which means they can produce fluent but unsupported claims.",
            "Retrieval-augmented generation can complement an LLM by supplying external, task-specific context at inference time instead of requiring all information to be encoded in model parameters."
        ]
    },

    {
        "question": "What is tokenization in LLMs?",
        "topic": "llm",
        "concepts": ["tokenization", "tokens", "vocabulary"],
        "incorrect": [
            "Tokenization trains the neural network weights.",
            "It converts every sentence into exactly one token.",
            "Tokenization is the same as model evaluation.",
            "It removes all words from text."
        ],
        "weak": [
            "Tokenization splits text.",
            "It creates tokens.",
            "LLMs use tokens instead of words.",
            "It prepares text for a model."
        ],
        "partial": [
            "Tokenization converts text into smaller units called tokens that a model can process.",
            "Tokens can represent words, subwords, characters, or byte-level pieces depending on the tokenizer.",
            "Each token is mapped to an integer ID.",
            "Tokenization affects sequence length and vocabulary size."
        ],
        "good": [
            "Tokenization converts raw text into token units and maps them to vocabulary IDs that an LLM can process.",
            "Modern LLM tokenizers often use subword or byte-level methods so uncommon words can be represented without requiring every complete word in the vocabulary.",
            "Different tokenizers can produce different token counts for the same text, which affects context length and cost.",
            "Special tokens can represent boundaries, padding, roles, or other structural information."
        ],
        "excellent": [
            "Tokenization is the preprocessing step that maps text into discrete tokens from a model-specific vocabulary. Depending on the tokenizer, tokens may correspond to words, subwords, characters, or byte-level units.",
            "Subword tokenization balances vocabulary size and the ability to represent rare or unseen words. The tokenizer maps tokens to integer IDs that become inputs to the model's embedding layer.",
            "Tokenization directly affects context-window usage, inference cost, and truncation behavior. Two models can tokenize the same sentence into different numbers of tokens.",
            "A tokenizer and its vocabulary are coupled to the model architecture and training process, so using the wrong tokenizer can produce invalid or poorly interpreted model inputs."
        ]
    },

    {
        "question": "What is prompt engineering?",
        "topic": "llm",
        "concepts": ["prompt-engineering", "instructions", "llm"],
        "incorrect": [
            "Prompt engineering changes neural network weights directly.",
            "It is only about changing the font.",
            "Prompt engineering trains an LLM from scratch.",
            "Prompts are irrelevant to model behavior."
        ],
        "weak": [
            "Prompt engineering means writing better prompts.",
            "It gives instructions to AI.",
            "It helps get better answers.",
            "It structures questions."
        ],
        "partial": [
            "Prompt engineering designs instructions and context to guide an LLM toward useful outputs.",
            "It can specify the role, task, constraints, examples, and desired output format.",
            "Clear prompts can reduce ambiguity.",
            "Few-shot examples are one prompt-engineering technique."
        ],
        "good": [
            "Prompt engineering involves designing instructions, context, constraints, examples, and output formats to guide a language model's behavior.",
            "A good prompt clearly describes the task and can include relevant retrieved information or examples.",
            "Structured output instructions can make model responses easier for software to parse.",
            "Prompt engineering changes the input context rather than changing the model's learned parameters."
        ],
        "excellent": [
            "Prompt engineering is the deliberate design of model inputs to elicit reliable behavior. It can include system instructions, task descriptions, constraints, demonstrations, retrieved context, and an explicit output schema.",
            "Good prompts reduce ambiguity and specify what information the model should use or avoid. They should also account for model limitations such as context length and susceptibility to unsupported assumptions.",
            "Few-shot prompting provides examples of desired input-output behavior, while zero-shot prompting gives only instructions. Both can be useful depending on task complexity.",
            "In production systems, prompt engineering should be evaluated systematically rather than judged from a few examples. Versioned prompts, representative test cases, and structured outputs make behavior easier to monitor."
        ]
    },

    {
        "question": "What is temperature in LLM generation?",
        "topic": "llm",
        "concepts": ["temperature", "sampling", "generation"],
        "incorrect": [
            "Temperature changes the physical temperature of the GPU.",
            "Temperature determines the number of model layers.",
            "Temperature always improves factual accuracy.",
            "Temperature changes the training dataset."
        ],
        "weak": [
            "Temperature controls randomness.",
            "Higher temperature gives more random answers.",
            "Lower temperature is more predictable.",
            "It affects generation."
        ],
        "partial": [
            "Temperature changes how sharply the model's token probabilities are distributed during sampling.",
            "Lower temperature generally makes high-probability tokens more dominant.",
            "Higher temperature can produce more diverse outputs.",
            "Temperature does not directly add factual knowledge to the model."
        ],
        "good": [
            "Temperature scales generation logits before softmax. Lower values make the distribution more peaked, while higher values generally increase diversity.",
            "A low temperature is often useful for deterministic or structured tasks, while a higher value can encourage creative variation.",
            "Temperature affects sampling behavior rather than the model's underlying knowledge.",
            "Extremely high temperature can produce less coherent outputs, while extremely low temperature can make generation repetitive or rigid."
        ],
        "excellent": [
            "Temperature modifies logits before sampling, commonly as z/T before softmax. Lower T sharpens the probability distribution, making high-probability tokens more dominant; higher T flattens it and increases sampling diversity.",
            "Temperature changes stochastic decoding rather than model parameters or stored knowledge. It therefore cannot fix factual errors caused by missing information.",
            "For structured technical interviews, a relatively low temperature can improve consistency, while question-generation tasks may tolerate somewhat more diversity.",
            "Temperature interacts with other decoding methods such as top-k and nucleus sampling, so output behavior depends on the entire decoding configuration rather than temperature alone."
        ]
    },

    {
        "question": "What is fine-tuning an LLM?",
        "topic": "llm",
        "concepts": ["fine-tuning", "training", "adaptation"],
        "incorrect": [
            "Fine-tuning means changing the prompt only.",
            "Fine-tuning never changes model parameters.",
            "Fine-tuning is the same as searching the internet.",
            "Fine-tuning deletes pretraining."
        ],
        "weak": [
            "Fine-tuning trains a pretrained model more.",
            "It adapts an LLM.",
            "It teaches a specific task.",
            "It uses another dataset."
        ],
        "partial": [
            "Fine-tuning continues training a pretrained model on task- or domain-specific data.",
            "It updates some or all model parameters depending on the method.",
            "Fine-tuning can specialize behavior for a particular task.",
            "Parameter-efficient methods can reduce the number of trainable parameters."
        ],
        "good": [
            "Fine-tuning adapts a pretrained model using additional task- or domain-specific training examples.",
            "Full fine-tuning updates many or all model parameters, while methods such as LoRA train a smaller set of additional parameters.",
            "A good fine-tuning dataset should represent the target behavior and avoid contradictory or low-quality examples.",
            "Fine-tuning changes model parameters, unlike prompt engineering or RAG, which mainly modify inference-time context."
        ],
        "excellent": [
            "Fine-tuning adapts a pretrained language model by continuing optimization on a target dataset. Depending on the method, the entire model or a small set of additional parameters may be trained.",
            "Parameter-efficient fine-tuning methods such as LoRA add trainable low-rank adapters while keeping most base parameters frozen, reducing memory and storage requirements.",
            "Fine-tuning is useful for changing task behavior, style, or domain specialization, but it is not necessarily the best method for injecting frequently changing factual information. RAG can provide that information dynamically.",
            "Fine-tuning quality depends strongly on the target dataset, objective, evaluation procedure, and degree of domain mismatch. Poor data can cause the model to learn undesirable behavior."
        ]
    },

    {
        "question": "What is hallucination in an LLM?",
        "topic": "llm",
        "concepts": ["hallucination", "factuality", "generation"],
        "incorrect": [
            "Hallucination means the model always refuses to answer.",
            "Hallucination is a hardware failure.",
            "Hallucination means the model has perfect factual knowledge.",
            "It only occurs when a GPU overheats."
        ],
        "weak": [
            "Hallucination means the AI makes things up.",
            "The model can give wrong information.",
            "It may invent facts.",
            "Hallucination is an AI mistake."
        ],
        "partial": [
            "LLM hallucination occurs when a model generates information that is unsupported, fabricated, or factually incorrect.",
            "Fluent language does not guarantee factual correctness.",
            "RAG and grounding can reduce hallucinations for knowledge-based tasks.",
            "Careful prompting and verification can also help."
        ],
        "good": [
            "Hallucination is the generation of plausible-sounding but unsupported or incorrect information. It can occur because language models optimize generation probabilities rather than directly verifying facts.",
            "Retrieval-augmented generation can reduce hallucination by providing relevant external evidence in the prompt.",
            "Structured output and explicit grounding instructions can improve reliability but do not guarantee correctness.",
            "High model confidence or fluent wording should not be treated as proof that an answer is factual."
        ],
        "excellent": [
            "An LLM hallucination is an output that presents unsupported, fabricated, or incorrect information as if it were valid. Fluency and confidence are not reliable indicators of factual correctness.",
            "Hallucinations can arise because the model predicts likely token sequences rather than executing a guaranteed fact-checking procedure. Missing context, ambiguous prompts, and distribution gaps can increase the risk.",
            "RAG reduces some knowledge-related hallucinations by retrieving evidence and placing it in the generation context, but retrieval errors or poor grounding can still produce incorrect answers.",
            "Reliable systems should combine grounding with validation, source-aware prompting, structured outputs, evaluation datasets, and appropriate fallback behavior rather than assuming any single technique eliminates hallucination."
        ]
    },

    {
        "question": "What is zero-shot prompting?",
        "topic": "llm",
        "concepts": ["zero-shot", "prompting", "llm"],
        "incorrect": [
            "Zero-shot means training the model with zero parameters.",
            "It requires thousands of examples in every prompt.",
            "Zero-shot cannot use instructions.",
            "Zero-shot is a type of database."
        ],
        "weak": [
            "Zero-shot means no examples.",
            "The model gets only the task.",
            "It asks the model directly.",
            "It is a prompting method."
        ],
        "partial": [
            "Zero-shot prompting asks a model to perform a task without providing task-specific examples in the prompt.",
            "The prompt can still contain clear instructions and constraints.",
            "The model relies on capabilities learned during pretraining or instruction tuning.",
            "Zero-shot can work well for familiar tasks."
        ],
        "good": [
            "Zero-shot prompting provides instructions for a task without including worked examples of the desired input-output behavior.",
            "The model must infer the intended behavior from the instruction and its pretrained or instruction-tuned capabilities.",
            "It is useful when creating examples is expensive or when the task is simple enough to describe clearly.",
            "Zero-shot and few-shot prompting differ mainly in whether demonstrations are included."
        ],
        "excellent": [
            "Zero-shot prompting asks an LLM to perform a task from instructions alone, without task-specific demonstrations in the prompt. The model relies on capabilities learned during pretraining and instruction tuning.",
            "A zero-shot prompt can still be detailed: it may specify the role, input format, constraints, evaluation criteria, and expected output schema. 'Zero-shot' refers to the absence of examples, not the absence of instructions.",
            "Few-shot prompting adds representative examples to demonstrate the desired mapping and can improve performance when the task is difficult to describe precisely.",
            "Whether zero-shot is sufficient depends on model capability, task complexity, ambiguity, and domain. It should be validated empirically rather than assumed to work."
        ]
    },

    {
        "question": "What is few-shot prompting?",
        "topic": "llm",
        "concepts": ["few-shot", "prompting", "examples"],
        "incorrect": [
            "Few-shot means training with exactly one sample permanently.",
            "Few-shot removes examples from the prompt.",
            "Few-shot requires changing model weights.",
            "Few-shot is only used for image classification."
        ],
        "weak": [
            "Few-shot gives examples.",
            "It shows the model some answers.",
            "It helps the model understand the task.",
            "It is prompting with examples."
        ],
        "partial": [
            "Few-shot prompting includes a small number of examples in the prompt to demonstrate the desired behavior.",
            "The model uses the examples as context without necessarily updating its parameters.",
            "Examples can demonstrate output style or classification labels.",
            "Good examples should be representative and consistent."
        ],
        "good": [
            "Few-shot prompting gives an LLM several examples of inputs and desired outputs within the prompt, allowing it to infer the task pattern without parameter updates.",
            "Examples can clarify formatting, classification boundaries, reasoning style, or domain-specific terminology.",
            "Poor or contradictory examples can degrade performance, so demonstrations should be carefully selected.",
            "Few-shot prompting increases context usage because the examples consume tokens."
        ],
        "excellent": [
            "Few-shot prompting provides a small set of demonstrations in the model context so the LLM can infer the desired mapping or output style at inference time. Unlike fine-tuning, it does not permanently update model parameters.",
            "Examples are especially useful when the task is ambiguous or when labels have nuanced semantics. They should cover representative cases and avoid inconsistent instructions.",
            "The main tradeoff is context consumption: every demonstration uses part of the model's context window and can increase latency or cost.",
            "Few-shot prompting can be viewed as in-context learning. The model adapts its behavior for the current prompt without changing its underlying parameters."
        ]
    },

    {
        "question": "What is structured output from an LLM?",
        "topic": "llm",
        "concepts": ["structured-output", "json", "parsing"],
        "incorrect": [
            "Structured output means the model can only answer with paragraphs.",
            "It prevents the model from generating text.",
            "It changes the neural network architecture.",
            "Structured output means random formatting."
        ],
        "weak": [
            "It makes the output structured.",
            "JSON is an example.",
            "It helps programs read AI responses.",
            "It gives a fixed format."
        ],
        "partial": [
            "Structured output constrains or requests an LLM response to follow a machine-readable schema such as JSON.",
            "It makes integration with backend code easier.",
            "A schema can specify fields and expected types.",
            "Validation can detect malformed responses."
        ],
        "good": [
            "Structured output makes an LLM return data in a predefined machine-readable format, such as JSON with specified fields and types.",
            "It is useful when an application needs to parse model results programmatically.",
            "Schema validation can reject or repair invalid responses before they reach application logic.",
            "For an interview evaluator, structured output can contain score, feedback, correctness, and suggested follow-up."
        ],
        "excellent": [
            "Structured output constrains an LLM response to a machine-readable schema, commonly JSON or a typed object. This reduces ambiguity when application code needs to consume model-generated data.",
            "A robust system should validate the returned structure and handle cases where the model produces malformed or incomplete content rather than assuming parsing will always succeed.",
            "Structured output is particularly useful for agent workflows: one node can return fields such as score, reasoning summary, next difficulty, and follow-up question that another node consumes.",
            "Schema-constrained generation improves interface reliability but does not guarantee semantic correctness. A valid JSON object can still contain incorrect or unsupported information."
        ]
    },

    {
        "question": "What is inference in machine learning?",
        "topic": "llm",
        "concepts": ["inference", "prediction", "deployment"],
        "incorrect": [
            "Inference means training the model from random initialization.",
            "Inference always changes model weights.",
            "Inference creates the dataset.",
            "Inference is only data preprocessing."
        ],
        "weak": [
            "Inference means using a trained model.",
            "It produces predictions.",
            "It happens after training.",
            "Inference gives output."
        ],
        "partial": [
            "Inference is the process of using trained model parameters to produce predictions or generated outputs for new inputs.",
            "Inference normally does not update model weights.",
            "LLM text generation is an inference process.",
            "Inference latency and memory usage matter in deployment."
        ],
        "good": [
            "Inference uses a trained model to produce outputs for new inputs without performing parameter updates.",
            "For an LLM, inference includes processing the prompt and generating tokens according to a decoding strategy.",
            "Production inference must consider latency, throughput, memory, batching, and hardware.",
            "Training and inference can use different computational optimizations."
        ],
        "excellent": [
            "Inference is the execution phase in which a trained model maps new input data to predictions or generated outputs using fixed parameters. In standard inference, gradients are not required and model weights are not updated.",
            "For autoregressive LLMs, inference includes a prompt-processing phase followed by iterative token generation. KV caching can reduce repeated computation during generation.",
            "Production inference involves tradeoffs among latency, throughput, memory, batching, quantization, hardware, and model size.",
            "Inference behavior can still be stochastic for generative models because decoding may sample from probability distributions even though the underlying model parameters remain unchanged."
        ]
    },

    # ========================================================
    # RAG — 10 QUESTIONS
    # ========================================================

    {
        "question": "Why is RAG useful for LLM applications?",
        "topic": "rag",
        "concepts": ["rag", "grounding", "retrieval"],
        "incorrect": [
            "RAG permanently retrains the LLM every time a user asks a question.",
            "RAG removes the need for any language model.",
            "RAG only compresses PDFs.",
            "RAG guarantees that every answer is correct."
        ],
        "weak": [
            "RAG gives the model more information.",
            "It searches documents.",
            "It helps answer questions.",
            "RAG uses external data."
        ],
        "partial": [
            "RAG retrieves relevant information from an external knowledge source and provides it to the LLM as context.",
            "It can ground responses in documents that were not part of the model's original training.",
            "RAG is useful for private, current, or domain-specific information.",
            "Retrieval quality strongly affects the final answer."
        ],
        "good": [
            "Retrieval-augmented generation retrieves relevant document chunks and includes them in the LLM prompt so the model can generate a grounded response.",
            "RAG is useful when information changes frequently or comes from private documents, because the knowledge source can be updated without retraining the LLM.",
            "A typical RAG pipeline contains document ingestion, chunking, embedding, vector indexing, retrieval, prompt construction, and generation.",
            "RAG can reduce hallucination but cannot guarantee correctness if retrieval or source documents are poor."
        ],
        "excellent": [
            "RAG separates knowledge retrieval from language generation. A retriever selects relevant external passages, and the LLM conditions its response on those passages at inference time.",
            "This architecture is useful for private or changing information because documents can be updated in the retrieval store without retraining the base LLM. It can also provide evidence that the application can cite or inspect.",
            "A complete RAG pipeline commonly includes parsing, chunking, metadata creation, embedding, indexing, query embedding, retrieval, optional reranking, context construction, and generation.",
            "RAG does not automatically solve hallucination. Poor chunking, irrelevant retrieval, missing information, or an LLM ignoring context can still produce incorrect answers, so retrieval and generation quality should be evaluated separately."
        ]
    },

    {
        "question": "What is a vector database?",
        "topic": "rag",
        "concepts": ["vector-database", "embeddings", "retrieval"],
        "incorrect": [
            "A vector database stores only SQL tables.",
            "It can store vectors but cannot search them.",
            "A vector database is a language model.",
            "It converts every vector into text."
        ],
        "weak": [
            "It stores embeddings.",
            "It searches vectors.",
            "It is used in RAG.",
            "It stores numerical data."
        ],
        "partial": [
            "A vector database stores embedding vectors and supports similarity search.",
            "It can retrieve documents whose embeddings are similar to a query embedding.",
            "Metadata can often be stored alongside vectors.",
            "Vector databases are commonly used in RAG systems."
        ],
        "good": [
            "A vector database indexes embedding vectors so that a query vector can efficiently retrieve semantically similar records.",
            "It commonly stores metadata and references to the original document chunks along with embeddings.",
            "Similarity can be measured using cosine similarity, dot product, or Euclidean distance depending on the embedding setup.",
            "Vector databases provide indexing methods that make similarity search practical at scale."
        ],
        "excellent": [
            "A vector database stores dense representations of objects and provides approximate or exact nearest-neighbor search over those vectors. In RAG, a query embedding is compared with document embeddings to retrieve relevant chunks.",
            "Besides vectors, a production system often stores metadata such as document ID, page number, section, source, or permissions so retrieval can be filtered and citations can be reconstructed.",
            "Similarity metrics must match the embedding model and indexing assumptions. Cosine similarity, inner product, and Euclidean distance are common choices.",
            "For small datasets, an in-memory index such as FAISS can be sufficient. Larger applications may use dedicated vector databases that provide persistence, filtering, distributed indexing, and operational features."
        ]
    },

    {
        "question": "Why is chunking important in RAG?",
        "topic": "rag",
        "concepts": ["chunking", "retrieval", "context"],
        "incorrect": [
            "Chunking means deleting half the document.",
            "RAG works best when every document is one token.",
            "Chunking has no effect on retrieval.",
            "Chunking changes the LLM weights."
        ],
        "weak": [
            "Chunking splits documents.",
            "It makes documents smaller.",
            "It helps retrieval.",
            "Chunks are pieces of text."
        ],
        "partial": [
            "Chunking divides documents into smaller pieces that can be embedded and retrieved independently.",
            "Very large chunks may contain too much irrelevant information.",
            "Very small chunks may lose important context.",
            "Chunk size and overlap affect retrieval quality."
        ],
        "good": [
            "Chunking divides source documents into retrieval units. Good chunk sizes balance enough context for understanding with enough specificity for relevant retrieval.",
            "If chunks are too large, retrieved context may contain irrelevant information and consume the LLM context window. If too small, important context can be separated.",
            "Overlap can preserve information across chunk boundaries.",
            "Semantic or structure-aware chunking can sometimes outperform fixed character or token lengths."
        ],
        "excellent": [
            "Chunking determines the granularity at which a RAG system indexes and retrieves knowledge. The goal is to create chunks that are semantically coherent enough to answer questions while remaining focused enough for accurate retrieval.",
            "Chunks that are too large dilute similarity and waste context-window capacity; chunks that are too small can remove definitions, assumptions, or relationships needed to interpret the retrieved passage.",
            "Overlap can reduce boundary loss, but excessive overlap increases index size and redundant retrieval. Document structure such as headings, paragraphs, pages, and sections can provide useful chunk boundaries.",
            "Chunking should be evaluated with the target retrieval workload rather than selected only by a generic token count. Different document types may require different strategies."
        ]
    },

    {
        "question": "What is semantic search?",
        "topic": "rag",
        "concepts": ["semantic-search", "embeddings", "similarity"],
        "incorrect": [
            "Semantic search only matches exact spelling.",
            "It ignores meaning completely.",
            "Semantic search is a text editor.",
            "It requires every query to have the same words as the document."
        ],
        "weak": [
            "It searches by meaning.",
            "It finds similar text.",
            "Embeddings are used.",
            "It is better than keyword search."
        ],
        "partial": [
            "Semantic search uses embeddings to retrieve text with similar meaning rather than relying only on exact keywords.",
            "A query and documents are converted into vectors.",
            "Similarity between vectors determines ranking.",
            "Semantic search can find relevant text even when wording differs."
        ],
        "good": [
            "Semantic search represents queries and documents as embeddings and retrieves items based on vector similarity, allowing conceptually related text to match even when exact words differ.",
            "It is useful for natural-language queries and RAG because relevant passages may use different terminology from the question.",
            "Cosine similarity or inner product can be used to rank embeddings.",
            "Semantic search can miss exact identifiers or rare keywords, which is one reason hybrid retrieval can be useful."
        ],
        "excellent": [
            "Semantic search uses learned vector representations to compare the meaning or task-relevant semantics of a query and candidate documents. It can retrieve conceptually related text even when vocabulary differs.",
            "A query encoder produces an embedding, and an index returns nearest document vectors according to a similarity metric. The retrieved chunks are then passed to downstream ranking or generation.",
            "Semantic retrieval is powerful for natural language but can struggle with exact identifiers, product codes, names, or rare terms. Combining vector retrieval with lexical methods can address these weaknesses.",
            "Retrieval quality depends on the embedding model, domain, chunking strategy, query formulation, similarity metric, and index configuration."
        ]
    },

    {
        "question": "What is a retriever in RAG?",
        "topic": "rag",
        "concepts": ["retriever", "retrieval", "rag"],
        "incorrect": [
            "A retriever generates the final answer without any model.",
            "It only cleans PDF formatting.",
            "A retriever trains the embedding model every query.",
            "It is the same as a database table."
        ],
        "weak": [
            "A retriever finds documents.",
            "It retrieves relevant chunks.",
            "It searches the knowledge base.",
            "It is part of RAG."
        ],
        "partial": [
            "A retriever selects relevant documents or chunks for a query.",
            "It can use vector similarity, keyword search, or both.",
            "The retrieved context is passed to the generation model.",
            "Retriever quality affects RAG answer quality."
        ],
        "good": [
            "The retriever is the RAG component responsible for selecting relevant source chunks for a user query.",
            "It may use dense vector search, lexical search, or hybrid retrieval.",
            "The retriever normally returns the top-k candidates, which may then be reranked before being placed in the LLM context.",
            "A strong generator cannot reliably answer from documents that the retriever failed to retrieve."
        ],
        "excellent": [
            "A RAG retriever maps a query to a ranked set of candidate knowledge chunks. Dense retrievers typically compare query and document embeddings, while lexical retrievers use token or term matching.",
            "The retriever's job is relevance, not final answer generation. Retrieved candidates may be passed through a reranker that uses richer query-document interactions before context construction.",
            "Top-k selection creates a recall-versus-context tradeoff: too few candidates can miss evidence, while too many can introduce noise and exceed the model's useful context capacity.",
            "Retriever evaluation can be performed independently using metrics such as recall@k, precision@k, and ranking metrics before evaluating the complete RAG generation pipeline."
        ]
    },

    {
        "question": "What is reranking in RAG?",
        "topic": "rag",
        "concepts": ["reranking", "retrieval", "ranking"],
        "incorrect": [
            "Reranking means randomly changing retrieved documents.",
            "It deletes all retrieved chunks.",
            "Reranking trains the LLM during every query.",
            "It is the same as PDF extraction."
        ],
        "weak": [
            "Reranking sorts documents again.",
            "It improves retrieval.",
            "A reranker chooses better results.",
            "It is another search step."
        ],
        "partial": [
            "Reranking takes an initial set of retrieved candidates and orders them again using a stronger relevance model.",
            "It can improve the quality of the top results.",
            "A cross-encoder is one possible reranking model.",
            "Reranking usually happens after fast initial retrieval."
        ],
        "good": [
            "Reranking refines the order of an initial candidate set using a more expensive relevance model, often improving which passages appear at the top.",
            "A common architecture uses vector or lexical retrieval for fast candidate generation followed by a cross-encoder reranker.",
            "Because reranking is more computationally expensive, it is usually applied to a limited candidate set rather than the entire corpus.",
            "Reranking can improve context quality without changing the underlying document embeddings."
        ],
        "excellent": [
            "Reranking is a second-stage retrieval step in which an initial candidate set is scored using a more expressive query-document relevance model. The goal is to improve the ordering of the most useful passages.",
            "A bi-encoder can efficiently embed queries and documents independently for initial retrieval, while a cross-encoder can jointly process a query and candidate passage to obtain a more precise relevance score.",
            "The tradeoff is latency: reranking every document would be expensive, so systems typically retrieve a moderate top-k candidate set first and rerank only those candidates.",
            "Reranking is especially valuable when dense retrieval finds broadly relevant candidates but their ordering is not precise enough for the limited context window available to the generator."
        ]
    },

    {
        "question": "How can a resume be used in a RAG system?",
        "topic": "rag",
        "concepts": ["resume", "pdf", "rag", "personalization"],
        "incorrect": [
            "A resume must be converted into model weights before RAG can use it.",
            "RAG cannot process resumes.",
            "The resume should always be sent as raw binary data to the LLM.",
            "A resume can only be used to generate the candidate's name."
        ],
        "weak": [
            "The resume is uploaded and searched.",
            "RAG reads the resume.",
            "Resume text becomes context.",
            "It helps personalize questions."
        ],
        "partial": [
            "A resume PDF can be parsed into text, split into chunks, embedded, and stored for retrieval.",
            "When generating an interview question, relevant resume chunks can be retrieved.",
            "This allows questions to reference the candidate's skills or projects.",
            "Metadata such as page numbers can help trace retrieved information."
        ],
        "good": [
            "A resume can be extracted with a PDF parser, chunked into sections, embedded, and indexed. During the interview, the system retrieves relevant chunks to personalize questions.",
            "For example, if a resume contains a machine-learning project, the retriever can return that section and the LLM can generate a question specifically about the project.",
            "Metadata such as page number, section, and source file should be stored with chunks so retrieved evidence can be traced.",
            "RAG is preferable to putting the entire resume into every prompt because retrieval selects only the most relevant information."
        ],
        "excellent": [
            "A resume-RAG pipeline can parse the uploaded PDF into text, preserve useful metadata such as page and section, split the text into coherent chunks, generate embeddings, and store those chunks in a vector index.",
            "When the interviewer needs a personalized question, the candidate profile or question-generation query can retrieve the most relevant resume sections. The LLM can then generate a question grounded in those sections.",
            "Retrieval should preserve provenance so the system can distinguish facts actually present in the resume from assumptions generated by the LLM. This is especially important for claims about projects, skills, or experience.",
            "For small interview sessions, an in-memory FAISS index can be sufficient. The architecture can later move to a persistent vector database without changing the conceptual RAG pipeline."
        ]
    },

    {
        "question": "What is hybrid retrieval in RAG?",
        "topic": "rag",
        "concepts": ["hybrid-retrieval", "bm25", "vector-search"],
        "incorrect": [
            "Hybrid retrieval uses only one retrieval algorithm.",
            "It combines model training with GPU cooling.",
            "Hybrid retrieval means retrieving random documents.",
            "It cannot use keyword search."
        ],
        "weak": [
            "Hybrid retrieval uses two searches.",
            "It combines retrieval methods.",
            "It can use keywords and vectors.",
            "It is useful in RAG."
        ],
        "partial": [
            "Hybrid retrieval combines lexical and semantic retrieval methods.",
            "BM25 can provide keyword matching while vector search captures semantic similarity.",
            "Combining the results can improve retrieval for different query types.",
            "Hybrid retrieval is useful when exact terms and semantic meaning both matter."
        ],
        "good": [
            "Hybrid retrieval combines lexical search, such as BM25, with dense vector search to capture both exact term matches and semantic similarity.",
            "Lexical search is useful for rare names, identifiers, and exact terminology, while embeddings can handle paraphrases and conceptually related text.",
            "The two result sets can be combined using score normalization, rank fusion, or another aggregation method.",
            "Hybrid retrieval can be more robust than relying on only one retrieval strategy."
        ],
        "excellent": [
            "Hybrid retrieval combines complementary retrieval signals, commonly sparse lexical matching such as BM25 with dense embedding similarity. This helps when a query contains both exact identifiers and conceptual language.",
            "BM25 is strong for rare or exact terms, while dense retrieval can connect paraphrases and semantically related wording. A fusion method can combine the rankings or scores.",
            "Reciprocal rank fusion is one practical way to combine ranked lists without requiring the scores from different retrievers to be directly comparable.",
            "Hybrid retrieval increases system complexity and can add latency, so it should be justified by retrieval evaluation on representative queries rather than added automatically."
        ]
    },

    {
        "question": "Why store metadata with RAG chunks?",
        "topic": "rag",
        "concepts": ["metadata", "provenance", "filtering"],
        "incorrect": [
            "Metadata replaces the actual chunk text.",
            "Metadata is only used to increase embedding dimensions.",
            "Metadata prevents retrieval.",
            "Metadata means the LLM's model weights."
        ],
        "weak": [
            "Metadata stores extra information.",
            "It identifies chunks.",
            "It can store page numbers.",
            "Metadata helps RAG."
        ],
        "partial": [
            "Metadata can store information such as document ID, page number, section, or source.",
            "It helps trace retrieved information back to its source.",
            "Metadata can also support filtering during retrieval.",
            "It can improve debugging and citations."
        ],
        "good": [
            "RAG metadata provides provenance and filtering information for each chunk, such as filename, page, section, candidate ID, or document type.",
            "It allows the application to identify where retrieved evidence came from and can support source citations.",
            "Metadata filters can prevent retrieval from unrelated documents or unauthorized sources.",
            "Separating metadata from chunk text keeps the retrieval representation flexible."
        ],
        "excellent": [
            "Metadata associates each indexed chunk with structured information such as document ID, page number, section, timestamp, candidate ID, permissions, or source URL. This enables provenance, filtering, and debugging.",
            "In a resume-RAG system, page and section metadata can allow the interviewer to explain which part of the resume supported a personalized question.",
            "Metadata can also enforce retrieval constraints, such as retrieving only chunks belonging to the current candidate or documents the user is authorized to access.",
            "Good metadata design is part of RAG architecture rather than an afterthought because retrieval relevance alone does not guarantee that the selected document is valid for the current user or task."
        ]
    },

    {
        "question": "How should RAG systems be evaluated?",
        "topic": "rag",
        "concepts": ["rag-evaluation", "retrieval", "generation"],
        "incorrect": [
            "RAG evaluation only checks whether the API starts.",
            "A RAG system is successful if it always generates long answers.",
            "Only the embedding dimension needs to be measured.",
            "RAG cannot be evaluated quantitatively."
        ],
        "weak": [
            "Check whether answers are good.",
            "Test the retrieval.",
            "See if the model answers questions.",
            "Evaluation checks RAG quality."
        ],
        "partial": [
            "RAG should evaluate retrieval quality and final answer quality separately.",
            "Retrieval metrics can include recall@k and precision@k.",
            "Generation can be evaluated for correctness, relevance, and groundedness.",
            "A representative test dataset is needed for meaningful evaluation."
        ],
        "good": [
            "A RAG system should separately evaluate retrieval and generation. Retrieval can use metrics such as recall@k, precision@k, and MRR, while generation can evaluate correctness, relevance, and faithfulness to retrieved evidence.",
            "End-to-end evaluation should include questions with known supporting documents and expected answer criteria.",
            "Failure analysis should distinguish retrieval failures from generation failures.",
            "Human evaluation can complement automated metrics for nuanced questions."
        ],
        "excellent": [
            "RAG evaluation should be decomposed into retrieval and generation because a wrong answer can result either from retrieving the wrong evidence or from reasoning poorly over correct evidence.",
            "Retrieval can be measured with recall@k, precision@k, MRR, or nDCG against known relevant passages. Generation can be assessed for factual correctness, relevance, completeness, and faithfulness to the retrieved context.",
            "An end-to-end benchmark should contain representative queries, expected evidence, and evaluation criteria. It should also include difficult cases such as missing information, ambiguous queries, and distractor documents.",
            "For production systems, latency, retrieval cost, context size, failure rates, and user feedback should be monitored alongside answer-quality metrics."
        ]
    },

    # ========================================================
    # FASTAPI / LANGGRAPH / SYSTEM DESIGN — 10 QUESTIONS
    # ========================================================

    {
        "question": "What is FastAPI?",
        "topic": "backend",
        "concepts": ["fastapi", "api", "python"],
        "incorrect": [
            "FastAPI is a database engine.",
            "FastAPI is an operating system.",
            "FastAPI can only create desktop applications.",
            "FastAPI replaces Python."
        ],
        "weak": [
            "FastAPI creates APIs.",
            "It is a Python framework.",
            "It is used for backend development.",
            "FastAPI handles web requests."
        ],
        "partial": [
            "FastAPI is a Python web framework for building APIs.",
            "It uses Python type hints and supports automatic API documentation.",
            "It can handle HTTP requests and return JSON responses.",
            "FastAPI is commonly used for machine-learning backends."
        ],
        "good": [
            "FastAPI is a Python framework for building HTTP APIs with type-hint-based validation and automatic OpenAPI documentation.",
            "It supports asynchronous endpoints and integrates with Pydantic for request and response validation.",
            "It is useful for exposing machine-learning or LLM functionality as backend services.",
            "Interactive documentation is commonly available through Swagger UI."
        ],
        "excellent": [
            "FastAPI is a modern Python framework for building HTTP APIs. It uses Python type hints and Pydantic-based validation to define request and response schemas and automatically generates an OpenAPI specification.",
            "It supports both synchronous and asynchronous endpoint functions, making it useful for services that perform I/O such as model APIs, databases, and external LLM calls.",
            "FastAPI's dependency-injection system can manage reusable concerns such as authentication, configuration, and database sessions.",
            "For an AI interviewer, FastAPI can expose endpoints for resume upload, interview creation, submitting answers, retrieving reports, and streaming interview events."
        ]
    },

    {
        "question": "What is an API endpoint?",
        "topic": "backend",
        "concepts": ["api", "endpoint", "http"],
        "incorrect": [
            "An endpoint is the last line of Python code.",
            "It is only a database column.",
            "An API endpoint cannot receive input.",
            "An endpoint is a neural network layer."
        ],
        "weak": [
            "An endpoint is an API URL.",
            "It receives requests.",
            "It gives responses.",
            "It is used by clients."
        ],
        "partial": [
            "An API endpoint is a specific network-accessible operation identified by a URL and HTTP method.",
            "For example, POST /interviews could create an interview.",
            "Endpoints define how clients interact with backend functionality.",
            "Requests and responses usually use structured data such as JSON."
        ],
        "good": [
            "An API endpoint represents a specific operation exposed by a service, usually identified by an HTTP method and route such as GET /interviews/{id}.",
            "The endpoint receives a request, validates inputs, performs backend logic, and returns a response.",
            "Different HTTP methods communicate intent such as GET for retrieval and POST for creating data.",
            "Clear endpoint contracts make frontend-backend integration easier."
        ],
        "excellent": [
            "An API endpoint is a defined interface through which a client invokes a backend operation. Its contract normally includes the HTTP method, path, request schema, authentication requirements, response schema, and possible error responses.",
            "For example, POST /interviews can accept candidate information and create a session, while POST /interviews/{id}/answer can submit an answer for evaluation.",
            "HTTP status codes communicate outcomes such as successful creation, invalid input, authentication failure, missing resources, or server errors.",
            "Well-designed endpoints separate transport concerns from application logic so the same interview engine can be reused by a web frontend, mobile client, or automated test."
        ]
    },

    {
        "question": "What is asynchronous programming in Python?",
        "topic": "backend",
        "concepts": ["async", "await", "concurrency"],
        "incorrect": [
            "Async programming means the code can never wait.",
            "async deletes all threads.",
            "await makes code execute twice.",
            "Asynchronous programming is only for machine learning training."
        ],
        "weak": [
            "Async lets tasks run together.",
            "It is useful for waiting.",
            "Python uses async and await.",
            "It can make servers faster."
        ],
        "partial": [
            "Asynchronous programming allows a program to perform other work while waiting for I/O operations.",
            "Python uses async and await for asynchronous coroutines.",
            "Async is especially useful for network and file I/O.",
            "Async concurrency is different from CPU parallelism."
        ],
        "good": [
            "Asynchronous programming allows an event loop to switch between tasks while one task is waiting for I/O, improving resource utilization for I/O-bound workloads.",
            "In Python, async def defines a coroutine and await pauses it until another asynchronous operation completes.",
            "Async does not automatically make CPU-heavy calculations parallel.",
            "FastAPI can use asynchronous endpoints when handling network-bound operations such as external LLM calls."
        ],
        "excellent": [
            "Python asynchronous programming uses coroutines and an event loop to interleave I/O-bound tasks without requiring a separate thread for every operation. async def defines a coroutine and await yields control while an awaitable is incomplete.",
            "This is valuable for web servers because an endpoint waiting for an external API can allow the event loop to handle other requests.",
            "Async concurrency is not the same as CPU parallelism. CPU-bound Python work may still require multiprocessing or native code that releases interpreter constraints.",
            "Using async incorrectly can reduce performance—for example, calling blocking I/O inside an async endpoint can block the event loop. Libraries used in an async path should therefore provide appropriate asynchronous interfaces when possible."
        ]
    },

    {
        "question": "What is LangGraph used for?",
        "topic": "agent",
        "concepts": ["langgraph", "workflow", "state"],
        "incorrect": [
            "LangGraph is a database for storing PDFs.",
            "LangGraph is a frontend CSS framework.",
            "LangGraph replaces the Python interpreter.",
            "LangGraph only performs tokenization."
        ],
        "weak": [
            "LangGraph builds AI workflows.",
            "It connects LLM steps.",
            "It manages agent workflows.",
            "It uses graphs."
        ],
        "partial": [
            "LangGraph is used to build stateful LLM workflows represented as graphs.",
            "Nodes perform operations and edges determine the flow between them.",
            "State can be passed between nodes.",
            "It is useful for multi-step agentic applications."
        ],
        "good": [
            "LangGraph represents an LLM application as a graph of stateful nodes and transitions, making multi-step workflows explicit.",
            "Nodes can generate questions, evaluate answers, retrieve documents, or call tools, while conditional edges can choose the next step.",
            "Checkpointing can preserve workflow state across interruptions or user interactions.",
            "This is useful for an interview system because the interview naturally consists of repeated question-answer-evaluation cycles."
        ],
        "excellent": [
            "LangGraph is a framework for building stateful, multi-step LLM workflows as directed graphs. Nodes perform operations on shared state and edges determine deterministic or conditional transitions.",
            "It is particularly useful when an application must pause for user input, branch based on model results, call tools, retry failures, or maintain state across multiple turns.",
            "Checkpointing allows a graph execution to resume from persisted state, which is useful for interactive interviews where the system waits for a candidate answer before continuing.",
            "For an AI interviewer, a graph can represent generate-question → wait-for-answer → evaluate → adapt-difficulty → continue/end, making the control flow easier to test than an unstructured chain of function calls."
        ]
    },

    {
        "question": "What is state in an LLM workflow?",
        "topic": "agent",
        "concepts": ["state", "workflow", "memory"],
        "incorrect": [
            "State means only the model's weights.",
            "State cannot contain user information.",
            "State is always stored inside the GPU.",
            "State means the HTTP status code only."
        ],
        "weak": [
            "State stores workflow information.",
            "It keeps track of progress.",
            "State remembers things.",
            "It contains variables."
        ],
        "partial": [
            "Workflow state contains information needed by different steps of an application.",
            "An interview state could contain the candidate, current question, answer, score, and difficulty.",
            "Nodes read and update state.",
            "State should contain information necessary for continuing the workflow."
        ],
        "good": [
            "State is the structured data carried through an LLM workflow. In an interview, it can contain candidate information, question history, current answer, evaluation, question number, and difficulty.",
            "Graph nodes read state and return updates to it.",
            "Explicit state makes multi-step workflows easier to reason about and resume.",
            "State is different from model weights and can be persisted independently."
        ],
        "excellent": [
            "Workflow state is the application-level data required to represent the current execution context. In an interview graph, it might include candidate profile, current question, answer history, evaluation results, question number, difficulty, and retrieved resume context.",
            "Nodes should update only the fields they are responsible for, while the graph controls how state flows between operations. This makes the workflow easier to test and debug.",
            "Persistent checkpointing can allow state to survive interruptions and resume later, while ephemeral state can be kept only for a single request or session.",
            "State design should avoid storing unnecessary sensitive data and should distinguish durable interview records from transient execution information."
        ]
    },

    {
        "question": "What is WebSocket communication?",
        "topic": "backend",
        "concepts": ["websocket", "realtime", "bidirectional"],
        "incorrect": [
            "WebSockets can only send files once.",
            "A WebSocket is a database index.",
            "WebSockets cannot keep connections open.",
            "WebSockets are only for CSS."
        ],
        "weak": [
            "WebSockets are for real-time communication.",
            "They keep a connection open.",
            "The server can send messages.",
            "They are useful for live apps."
        ],
        "partial": [
            "WebSockets provide persistent two-way communication between a client and server.",
            "Unlike ordinary request-response HTTP usage, either side can send messages after the connection is established.",
            "They are useful for real-time updates.",
            "AI interview progress can be sent through a WebSocket."
        ],
        "good": [
            "WebSockets establish a persistent bidirectional connection so the client and server can send messages without creating a new HTTP request for every update.",
            "They are useful for streaming events such as transcription, interviewer state, progress, and generated responses.",
            "A WebSocket server must handle connection lifecycle, errors, and disconnects.",
            "They can complement REST endpoints rather than replacing every HTTP API."
        ],
        "excellent": [
            "WebSocket communication establishes a long-lived bidirectional channel between client and server. After the initial handshake, either side can send messages asynchronously without a separate HTTP request for each event.",
            "This is useful for real-time AI applications where the backend may stream partial transcription, interview state changes, generated questions, or evaluation progress to the frontend.",
            "WebSockets introduce lifecycle and scaling concerns such as reconnects, authentication, connection limits, and session routing, so REST remains useful for durable operations such as creating interviews and fetching final reports.",
            "A practical interview architecture can use REST for session management and WebSockets for live interaction and streaming events."
        ]
    },

    {
        "question": "What is session management in a web application?",
        "topic": "backend",
        "concepts": ["session", "state", "authentication"],
        "incorrect": [
            "Session management only stores CSS settings.",
            "Sessions are the same as neural network layers.",
            "A session can never expire.",
            "Session management is unrelated to users."
        ],
        "weak": [
            "It keeps track of a user.",
            "Sessions store user progress.",
            "It manages login information.",
            "It remembers a session."
        ],
        "partial": [
            "Session management associates requests with a particular user or workflow.",
            "An interview session can identify the current candidate and interview state.",
            "Sessions may use IDs, cookies, tokens, or server-side storage.",
            "Secure systems should prevent unauthorized access to another user's session."
        ],
        "good": [
            "Session management maintains state across multiple requests or interactions by associating a client with a server-side or token-based session identifier.",
            "For an interview, a session ID can identify the candidate, current question, answer history, and interview progress.",
            "Sessions should have appropriate authentication, authorization, expiration, and cleanup policies.",
            "In-memory sessions are simple for development but persistent storage is needed when reliability or multiple backend instances matter."
        ],
        "excellent": [
            "Session management maintains continuity across otherwise independent requests by associating them with a session identity and corresponding application state. The state may be server-side or represented partly by signed tokens.",
            "An interview application can use a session ID to associate uploaded resume data, graph checkpoints, question history, and final results with the correct candidate.",
            "Authentication establishes who a user is, while authorization determines whether that user is allowed to access a particular session. These concerns should not be conflated.",
            "For scalable deployments, session state may need persistent storage or a shared state service rather than process-local memory, especially when multiple backend instances can receive requests."
        ]
    },

    {
        "question": "Why should backend APIs validate input?",
        "topic": "backend",
        "concepts": ["validation", "security", "api"],
        "incorrect": [
            "Input validation is unnecessary because clients are always trusted.",
            "Validation only improves screen colors.",
            "Validation means deleting user input.",
            "Backend validation can be skipped if frontend validation exists."
        ],
        "weak": [
            "Validation checks user input.",
            "It prevents bad data.",
            "It improves APIs.",
            "It checks fields."
        ],
        "partial": [
            "Backend validation ensures incoming data matches expected types and constraints.",
            "It protects the server even when a client sends malformed or malicious input.",
            "Frontend validation improves user experience but cannot replace backend validation.",
            "Schema validation can make API behavior more predictable."
        ],
        "good": [
            "Backend validation checks that requests conform to expected schemas and constraints before application logic processes them.",
            "It is necessary because clients cannot be trusted to send valid or safe input.",
            "FastAPI and Pydantic can validate request bodies and return clear errors for invalid data.",
            "Validation reduces bugs and can also contribute to security by rejecting unexpected input."
        ],
        "excellent": [
            "Backend input validation establishes a trusted application-level representation from untrusted client input. It verifies types, required fields, ranges, formats, and domain constraints before business logic executes.",
            "Frontend validation is useful for user experience but cannot be considered a security boundary because a client can bypass it and send arbitrary HTTP requests.",
            "Schema validation also improves API contracts: downstream code can rely on normalized structures instead of repeatedly checking raw request data.",
            "Validation should be combined with authentication, authorization, rate limiting, safe file handling, and output validation because no single validation layer provides complete security."
        ]
    },

    {
        "question": "What is caching in an AI application?",
        "topic": "backend",
        "concepts": ["caching", "latency", "performance"],
        "incorrect": [
            "Caching always makes systems slower.",
            "Caching means deleting old results.",
            "Caching changes the model weights.",
            "Cache data can never expire."
        ],
        "weak": [
            "Caching stores results.",
            "It makes responses faster.",
            "It avoids repeated work.",
            "It saves data temporarily."
        ],
        "partial": [
            "Caching stores reusable results so repeated requests can avoid expensive computation.",
            "AI applications can cache embeddings, model responses, or retrieved documents.",
            "Caching can reduce latency and cost.",
            "Cached data needs an invalidation strategy."
        ],
        "good": [
            "Caching stores reusable intermediate or final results so future requests can avoid repeating expensive work.",
            "An AI interviewer could cache resume embeddings or repeated retrieval results, while response caching should consider whether the candidate context has changed.",
            "Caching can reduce latency, API cost, and computational load.",
            "Cache invalidation and stale data are important design considerations."
        ],
        "excellent": [
            "Caching reuses previously computed results to reduce latency and resource consumption. AI systems can cache embeddings, retrieval results, prompt computations, or deterministic model outputs depending on the application.",
            "For a resume-RAG system, embeddings for an unchanged resume can be cached because recomputing them provides no benefit. Interview answers and adaptive questions generally require more careful cache keys because the session state changes.",
            "A cache requires a key strategy, expiration or invalidation policy, and consideration of consistency. Incorrect caching can return another candidate's information or stale results.",
            "Caching is therefore both a performance technique and a correctness concern in stateful AI applications."
        ]
    },

    {
        "question": "Why separate frontend and backend in an AI application?",
        "topic": "system-design",
        "concepts": ["frontend", "backend", "architecture"],
        "incorrect": [
            "Separation means the frontend cannot communicate with the backend.",
            "It prevents APIs from existing.",
            "It makes all applications single-user.",
            "Frontend and backend must use the same programming language."
        ],
        "weak": [
            "It keeps code organized.",
            "Frontend handles UI and backend handles logic.",
            "It is common architecture.",
            "They communicate through APIs."
        ],
        "partial": [
            "The frontend handles user interaction while the backend handles business logic, data, and model calls.",
            "They communicate through APIs such as REST or WebSockets.",
            "Separating them allows each side to evolve independently.",
            "The backend can protect API keys and model credentials."
        ],
        "good": [
            "A frontend/backend separation assigns UI and interaction responsibilities to the frontend while the backend manages business logic, authentication, storage, and AI model calls.",
            "The frontend communicates with the backend through defined APIs, which prevents secrets such as LLM API keys from being exposed in browser code.",
            "Each layer can be tested and deployed independently.",
            "This architecture also allows other clients to reuse the same backend."
        ],
        "excellent": [
            "Separating frontend and backend creates a clear boundary between presentation and server-side application logic. The React frontend handles UI state and user interaction, while FastAPI can handle interview orchestration, RAG, model calls, persistence, and security-sensitive operations.",
            "API contracts such as REST endpoints or WebSocket messages define the boundary between the two layers. This makes each side independently testable and replaceable.",
            "Secrets such as OpenRouter API keys must remain server-side rather than being embedded in browser JavaScript.",
            "The separation also supports multiple clients—for example, a web UI, mobile application, or automated test suite can all consume the same interview backend."
        ]
    },
]