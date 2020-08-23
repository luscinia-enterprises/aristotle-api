# aristotle-resources-service

Current functionality: CRUD for resources

Things to note in this current version:   
- When creating and updating resources, dates have to be in the ISODate format, or else a ValidationError will be thrown.

```
"publication": {
    "$date": "2019-09-30T00:00:00.000Z"
},
```
        
- UUID also has to be in the following format:
 
```
"uuid": {  
    "$uuid": "334a59ad577a822bf4b1b0ac3a910e80"
}
```

Sample Post/Put data:

```
{
    "_class": "ca.luscinia.aristotle.database.Resource",
    "content": "<h1>Introduction to Arithmetic Operations</h1><p style=\"margin-left:0px;\"><br><br>&nbsp;</p><h2 style=\"margin-left:0px;\"><strong>Basic Operations</strong></h2><p style=\"margin-left:0px;\">The basic arithmetic operations for real numbers are addition, subtraction, multiplication, and division.</p><h3 style=\"margin-left:0px;text-align:center;\"><strong>LEARNING OBJECTIVES</strong></h3><p style=\"margin-left:0px;\">Calculate the sum, difference, product, and quotient of positive whole numbers</p><h3 style=\"margin-left:0px;text-align:center;\"><strong>KEY TAKEAWAYS</strong></h3><h4 style=\"margin-left:0px;\"><strong>Key Points</strong></h4><ul><li>The basic arithmetic operations for real numbers are addition, subtraction, multiplication, and division.</li><li>The basic arithmetic properties are the commutative, associative, and distributive properties.</li></ul><h4 style=\"margin-left:0px;\"><strong>Key Terms</strong></h4><ul><li><strong>associative</strong>: Referring to a mathematical operation that yields the same result regardless of the grouping of the elements.</li><li><strong>commutative</strong>: Referring to a binary operation in which changing the order of the operands does not change the result (e.g., addition and multiplication).</li><li><strong>product</strong>: The result of multiplying two quantities.</li><li><strong>quotient</strong>: The result of dividing one quantity by another.</li><li><strong>sum</strong>: The result of adding two quantities.</li><li><strong>difference</strong>: The result of subtracting one quantity from another.</li></ul><h4 style=\"margin-left:0px;\"><strong>The Four Arithmetic Operations</strong></h4><h3 style=\"margin-left:0px;\"><strong>Addition</strong></h3><p style=\"margin-left:0px;\">Addition is the most basic operation of arithmetic. In its simplest form, addition combines two quantities into a single quantity, or <i>sum</i>. For example, say you have a group of 2 boxes and another group of 3 boxes. If you combine both groups together, you now have one group of 5 boxes. To represent this idea in mathematical terms:</p><p style=\"margin-left:0px;\">2+3=5<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p><h3 style=\"margin-left:0px;\"><strong>Subtraction</strong></h3><p style=\"margin-left:0px;\">Subtraction is the opposite of addition. Instead of adding quantities together, we are removing one quantity from another to find the <i>difference</i> between the two. Continuing the previous example, say you start with a group of 5 boxes. If you then remove 3 boxes from that group, you are left with 2 boxes. In mathematical terms:</p><p style=\"margin-left:0px;\">5−3=2<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mn>5</mn><mo>−</mo><mn>3</mn><mo>=</mo><mn>2</mn></math></p><h3 style=\"margin-left:0px;\"><strong>Multiplication</strong></h3><p style=\"margin-left:0px;\">Multiplication also combines multiple quantities into a single quantity, called the <i>product</i>. In fact, multiplication can be thought of as a consolidation of many additions. Specifically, the product of x<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>x</mi></math>&nbsp;and y<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>y</mi></math>&nbsp;is the result of x<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>x</mi></math>&nbsp;added together y<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>y</mi></math>&nbsp;times. For example, one way of counting four groups of two boxes is to add the groups together:</p><p style=\"margin-left:0px;\">2+2+2+2=8<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>8</mn></math></p><p style=\"margin-left:0px;\">However, another way to count the boxes is to multiply the quantities:</p><p style=\"margin-left:0px;\">2⋅4=8<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mn>2</mn><mo>⋅</mo><mn>4</mn><mo>=</mo><mn>8</mn></math></p><p style=\"margin-left:0px;\">Note that both methods give you the same result—8—but in many cases, particularly when you have large quantities or many groups, multiplying can be much faster.</p><h3 style=\"margin-left:0px;\"><strong>Division</strong></h3><p style=\"margin-left:0px;\">Division is the inverse of multiplication. Rather than multiplying quantities together to result in a larger value, you are splitting a quantity into a smaller value, called the <i>quotient</i>. Again, to return to the box example, splitting up a group of 8 boxes into 4 equal groups results in 4 groups of 2 boxes:</p><p style=\"margin-left:0px;\">8÷4=2<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mn>8</mn><mo>÷</mo><mn>4</mn><mo>=</mo><mn>2</mn></math></p>",
    "copyrightInfo": {
        "url": "https://courses.lumenlearning.com/boundless-algebra/chapter/introduction-to-arithmetic-operations/#:~:text=The%20order%20of%20operations%20is,as%20are%20addition%20and%20subtraction.",
        "author": "Lumen Learning",
        "publisher": "LumenCandela",
        "publication": {
            "$date": "2019-08-31T00:00:00.000Z"
        },
        "update": {
            "$date": "2017-08-31T00:00:00.000Z"
        },
        "location": "unknown"
    },
    "learningStyle": {
        "llss": 90,
        "slss": 60,
        "alss": 10,
        "klss": 10,
        "mlss": 80,
        "sms": -25,
        "qms": 44,
        "tms": 44
    },
    "name": "Introduction to Arithmetic Operations",
    "tags": {
        "subject": "Math",
        "gradeLevel": "9",
        "curriculum": "British Columbia",
        "majorTopic": [
            "Operations with Rational Numbers"
        ],
        "minorTopic": [
            "What is a rational number?",
            "Order of operations with rational numbers",
            "Adding rational numbers",
            "Subtracting rational numbers",
            "Multiplying rational numbers",
            "Dividing rational numbers",
            "Evaluating compound numerical expressions",
            "Rules of Arithmetic"
        ],
        "keywords": []
    },
    "uuid": {
        "$uuid": "334a59ad577a822bf4b1b0ac3a910e80"
    }
}
```

Next step:
- restructure program using flask-restful 