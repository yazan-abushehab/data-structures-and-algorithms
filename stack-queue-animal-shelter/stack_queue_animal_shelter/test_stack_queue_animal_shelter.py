from stack_queue_animal_shelter.stack_queue_animal_shelter import Animal, AnimalShelter


def test_enqueue_edge_case():
    shelter = AnimalShelter()
    dog1 = Animal("dog", "Buddy")

    shelter.enqueue(dog1)
    assert shelter.dogs == [dog1]
    assert shelter.cats == []

    # Enqueue another dog with same name but different timestamp
    dog2 = Animal("dog", "Buddy")
    shelter.enqueue(dog2)
    assert shelter.dogs == [dog1, dog2]
    assert shelter.cats == []


def test_dequeue_dog():
    shelter = AnimalShelter()
    dog1 = Animal("dog", "Buddy")
    cat1 = Animal("cat", "Whiskers")
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)

    # Dequeue a dog
    assert shelter.dequeue("dog") == dog1
    assert shelter.dogs == []
    assert shelter.cats == [cat1]


def test_dequeue_cat():
    shelter = AnimalShelter()
    dog1 = Animal("dog", "Buddy")
    cat1 = Animal("cat", "Whiskers")
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)

    # Dequeue a cat
    assert shelter.dequeue("cat") == cat1
    assert shelter.dogs == [dog1]
    assert shelter.cats == []


def test_dequeue_no_pref():
    shelter = AnimalShelter()
    dog1 = Animal("dog", "Buddy")
    cat1 = Animal("cat", "Whiskers")
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)

    # Dequeue without preference
    assert shelter.dequeue() == dog1
    assert shelter.dogs == []
    assert shelter.cats == [cat1]

    # Enqueue another dog and cat
    dog2 = Animal("dog", "Max")
    cat2 = Animal("cat", "Mittens")
    shelter.enqueue(dog2)
    shelter.enqueue(cat2)

    # Dequeue without preference again
    assert shelter.dequeue() == cat1
    assert shelter.dogs == [dog2]
    assert shelter.cats == [cat2]


def test_dequeue_no_animals():
    shelter = AnimalShelter()

    # Dequeue without any animals in the shelter
    assert shelter.dequeue("dog") is None
    assert shelter.dequeue("cat") is None
    assert shelter.dequeue() is None
