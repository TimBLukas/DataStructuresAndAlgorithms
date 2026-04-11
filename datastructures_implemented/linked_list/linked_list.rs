use std::boxed::Box;


struct Node<T> {
    val: T,
    next: Option<Box<Node<T>>>,
}

impl<T> Node<T> {
    fn new<S>(val: S) -> Node<S> {
        return Node {
            val: val,
            next: None
        }

    }
}


struct LinkedList<T> {
    head: Option<Box<Node<T>>>,
}

impl<T> LinkedList<T> {
    fn new<S>(head: Node<S>) -> LinkedList<S> {
        return LinkedList {
            head: head
        }
    }

    fn append(val: T) {
        let curr = self.head;
        while curr

    }

}



fn main() {

    println!("Hello world");
    let node = Node::<i32>::new(1);
}
