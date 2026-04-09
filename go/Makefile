BINARY_NAME=go-service

build:
	go build -o $(BINARY_NAME) main.go

test:
	go test -v ./...

run:
	go run main.go

clean:
	rm -f $(BINARY_NAME)

docker-build:
	docker build -t $(BINARY_NAME) .
